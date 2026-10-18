"""Built-up footprint from ESA WorldCover 10 m (class 50 = built-up, 80 = water), aggregated to 1/2400 deg cells (~46 m)."""
import os, math, time, json, sys
import numpy as np, pandas as pd, rasterio
from rasterio.windows import Window
from scipy import ndimage as ndi
os.environ.setdefault('GDAL_HTTP_PROXY', os.environ.get('HTTPS_PROXY',''))
os.environ.setdefault('GDAL_CURL_CA_BUNDLE','/root/.ccr/ca-bundle.crt')
os.environ['GDAL_DISABLE_READDIR_ON_OPEN']='EMPTY_DIR'
os.environ['CPL_VSIL_CURL_ALLOWED_EXTENSIONS']='.tif'
os.environ['GDAL_HTTP_MAX_RETRY']='4'; os.environ['GDAL_HTTP_RETRY_DELAY']='2'
os.environ['VSI_CACHE']='TRUE'; os.environ['VSI_CACHE_SIZE']=str(200*1024*1024)
BASE='https://esa-worldcover.s3.eu-central-1.amazonaws.com/v200/2021/map/ESA_WorldCover_10m_2021_v200_{ns}{lat:02d}{ew}{lon:03d}_Map.tif'
PX=12000      # WorldCover pixels per degree
AGG=5         # 5x5 px -> one cell (1/2400 deg)
CPD=PX//AGG   # cells per degree
_ds={}
def tile_url(lat,lon):
    return BASE.format(ns='N' if lat>=0 else 'S',lat=abs(lat),ew='E' if lon>=0 else 'W',lon=abs(lon))
def tile(lat,lon):
    k=(lat,lon)
    if k not in _ds:
        try: _ds[k]=rasterio.open(tile_url(lat,lon))
        except rasterio.errors.RasterioIOError: _ds[k]=None   # sea tile: not published
    return _ds[k]
def read_cells(c0,c1,r0,r1):
    """Cell-grid box [c0,c1) x [r0,r1) (global cell indices: col from lon -180, row from lat +90, row grows south).
    Returns (built, water) uint8 arrays with counts 0..25 per cell."""
    H,W=r1-r0,c1-c0
    built=np.zeros((H,W),np.uint8); water=np.zeros((H,W),np.uint8)
    # tiles are 3 deg = 3*CPD cells
    T=3*CPD
    for tr in range(r0//T, (r1-1)//T+1):
        for tc in range(c0//T, (c1-1)//T+1):
            lat=90-3*(tr+1); lon=-180+3*tc           # tile SW corner
            ds=tile(lat,lon)
            if ds is None: continue
            rr0,rr1=max(r0,tr*T),min(r1,(tr+1)*T); cc0,cc1=max(c0,tc*T),min(c1,(tc+1)*T)
            win=Window((cc0-tc*T)*AGG,(rr0-tr*T)*AGG,(cc1-cc0)*AGG,(rr1-rr0)*AGG)
            for attempt in range(4):
                try: a=ds.read(1,window=win); break
                except Exception as e:
                    if attempt==3: raise
                    time.sleep(2*(attempt+1))
            b=(a==50).reshape(rr1-rr0,AGG,cc1-cc0,AGG).sum((1,3)).astype(np.uint8)
            w=(a==80).reshape(rr1-rr0,AGG,cc1-cc0,AGG).sum((1,3)).astype(np.uint8)
            built[rr0-r0:rr1-r0,cc0-c0:cc1-c0]=b; water[rr0-r0:rr1-r0,cc0-c0:cc1-c0]=w
    return built,water
def cell_of(lon,lat): return int(math.floor((lon+180)*CPD)), int(math.floor((90-lat)*CPD))
def disk(ry,rx):
    y,x=np.ogrid[-ry:ry+1,-rx:rx+1]; return (y/max(ry,.5))**2+(x/max(rx,.5))**2<=1.0
def footprint(built,water,lat_mid,T=0.2,OPEN=100,CLOSE=350,HOLE_KM2=0.5,PIECE_KM2=0.25):
    """built/water: counts per cell. Returns mask (bool) after open/close/fill, plus water mask."""
    cy=110574/CPD; cx=111320*math.cos(math.radians(lat_mid))/CPD   # cell size in metres
    m=built>=round(T*AGG*AGG)
    if OPEN:
        s=disk(max(1,round(OPEN/cy)),max(1,round(OPEN/cx))); m=ndi.binary_opening(m,s)
    if CLOSE:
        s=disk(round(CLOSE/cy),round(CLOSE/cx)); m=ndi.binary_closing(m,s)
    # fill holes smaller than HOLE_KM2
    holes=~m; lab,n=ndi.label(holes)
    if n:
        sizes=ndi.sum(holes,lab,range(1,n+1))*cx*cy/1e6
        # holes touching the border are outside, not holes
        border=np.zeros(n+1,bool); border[np.unique(np.r_[lab[0],lab[-1],lab[:,0],lab[:,-1]])]=True
        small=np.r_[False,sizes<HOLE_KM2]&~border
        m|=small[lab]
    return m, cx, cy
