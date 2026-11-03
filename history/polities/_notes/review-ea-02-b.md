# Review of batch ea-02-b (six Eighteen Kingdoms rows)

Reviewer, 2026-10-19. Dossiers: han-2, henan, jiaodong, jiujiang, liaodong, linjiang. The machine copy is history/notes/phase-b/reviews/ea-02-b.json.

## Verdicts

| slug | verdict | in one line |
| --- | --- | --- |
| han-2 | fix | Dates hold (Xin of Han, Xiang Yu pages). Reviewer raised 201 relocation to confidence 3. Author still owes: vassal events 205-201 and the Luoyang basin taken out of the Hán outline. |
| henan | **fail** | Cliopatria's Henan polygon sits on Henei (Zhaoge, Yin's seat), not on Luoyang. The dossier said "with Luoyang inside", which is false. Keyframe 0 and ledger regions must be redrawn. |
| jiaodong | fix | All events confirmed. Reviewer renamed the war to qi's "Revolt of Tian Rong against the Three Qis" (206 only). |
| jiujiang | thin | Events honest; three confidence-1 events for the year of Long Ju's victory (no page dates it). Reviewer verified the capital Liu (zh 英布). |
| liaodong | fix | Events confirmed. Reviewer verified the capital Wuzhong (zh 韓廣), noted that it lies outside the outline, and renamed the war to "Zang Tu's conquest of Liaodong" (206). |
| linjiang | fix | Events confirmed (Gong Ao, Timeline). Author still owes: eastern Hubei taken out of the outline. The table gives that land to Hengshan (Wu Rui), which Cliopatria lacks. |

Mechanical checks: the validator passes all six with 0 errors, before and after the edits. han-2's nine "han_-404 ... has no verdict" warnings are a validator bug: slugify("Hán") gives "han", so it looks up the wrong rows. They are not a dossier fault.

## Findings the authors must act on

### henan (blocking)

- `/keyframe_review/0`. The verdict is adjust "years change, the outline does not", and the note says "with Luoyang inside". Neither holds:
  - Zh Wikipedia 申阳: "项羽分韩国为河南国,封申阳为河南王,建都洛阳" and "其地成为河南郡".
  - The English Shen Yang page: "granted part of the former Hán kingdom's territory".
  - Polygon test against the Cliopatria geojson:
    - Luoyang (112.47 E, 34.68 N) is 60 km outside the Henan polygon, inside Cliopatria's Hán. The bbox contains Luoyang; the polygon does not.
    - Only 11 percent of a 90 km disc around Luoyang lies in Henan. 95 percent of a 90 km disc around Zhaoge (114.2 E, 35.6 N; Sima Ang's Yin) does.
    - 78 percent of the shape lies north of 35.0 N, 75 percent east of 113.5 E.

  **Fix:**
  - Set the verdict to wrong (or adjust). Give a correction for the Luoyang kingdom (Qin Sanchuan, the later Henan Commandery), e.g. `{"place": "Luoyang", "km": 90, "text": "建都洛阳 ... 其地成为河南郡"}` or the north-west part of Cliopatria's Hán 206 shape.
  - Say that the Henei cells belong to Yin (ea-02-c).
  - Use the same region in ledger 0-2, the war zone and the predecessor/successor land.
- Applied by the reviewer: the capital's source is now the zh 申阳 page (added to sources), and its note was corrected. The war name is now "Chu-Han Contention" (hyphen, as in kingdom-of-han and western-chu).
- Info: zh gives the surrender as 汉二年(前205年)十一月. The 11th lunar month of Han year 2 falls around Dec 206 / Jan 205, which explains why the Timeline page files it under 206. No month stored; that is right.

### han-2 (non-blocking)

- **Missing vassal events.** The Xin of Han page says "He was made King of Hán (韓王) in 205 BC by Liu Bang" and "granted the lands around Yingchuan as his vassal kingdom". The ledger records this only as a rename, so the kingdom draws as independent. Cliopatria's Han 203 shape (kingdom-of-han han_-203) covers 88 percent of the Hán outline.
  - **Fix:** add vassal_start 205 / vassal_end 203 with counterpart kingdom-of-han, and vassal_start 202 / vassal_end 201 with counterpart han-dynasty. Mention the 88 percent overlap in keyframe 1.
- **Keyframe 0 (and 1) verdict ok.** The Hán polygon holds Luoyang, Henan's capital: 89 percent of the Luoyang disc, which is 22 percent of the Hán shape.
  - **Fix:** adjust, minus the Luoyang basin, coordinated with the henan correction.
- **Applied by the reviewer:**
  - Ledger 4 (gain of Taiyuan) and 5 (capital to Jinyang) raised to confidence 3. The page dates the move: "In 201 BC, Liu Bang realised that the Hán vassal kingdom was in a strategic location".
  - The ledger 4 and keyframe 2 notes were corrected to match.
  - War name hyphen.
- **Thin:** ledger 3 (who took Yingchuan in 201) is confidence 1.

### linjiang (non-blocking)

- **Keyframe 0 verdict ok, with the note "the shape follows the table".** The table gives Linjiang only "western Hubei, northern Hunan", and gives Hengshan (Wu Rui) "eastern Hubei, Jiangxi". The Wu Rui page: "In 206 BC, Wu Rui was bestowed the title King of Hengshan", tenure 206-March 202. Wuhan and Huanggang lie inside the Linjiang polygon, and 26 percent of it is east of 113.5 E.
  - **Fix:** adjust (also keyframe 1), minus eastern Hubei. Hengshan needs a dossier (suggested slug `hengshan`, 206-202; added to this review's counterparts list).
- **Applied by the reviewer:**
  - Keyframe 1 note: Cliopatria's Han 203 also covers 43 percent of the outline, besides Western Chu's 47 percent.
  - War name hyphen.
- **Thin:** ledger 1 (which force, which month, 202).

### jiujiang (thin)

- Ledger 2-4 are confidence 1 for the year Long Ju took Jiujiang. Long Ju's page has "In late 205 BC ... Xiang Yu sent Long Ju", and the Ying Bu page has "Months later". Zh 英布 is undated too ("战争持续了几个月").
- An upper bound: the Timeline puts Long Ju's death at the Wei River under 204 BC.
- Page to try: Shiji 91 (黥布列傳) on zh.wikisource.
- Applied by the reviewer: the capital Liu is now verified (zh 英布: "便立英布為九江王，以六為都"), and the war name has the hyphen.

### jiaodong and liaodong

- Every event confirmed.
- jiaodong: the reviewer replaced the 206-202 "Chu–Han Contention" war entry with qi's "Revolt of Tian Rong against the Three Qis" (206; belligerents qi, jiaodong, jibei).
- liaodong: the reviewer did the same with "Zang Tu's conquest of Liaodong" (206; yan, liaodong).
- liaodong's capital is now verified on zh 韓廣: "以無終(今天津薊縣)為都". The capital and keyframe 0 notes now say that Wuzhong lies about 160 km west of the Liaodong polygon, inside Yan's 206 shape. The outline is kept because Han Guang "不肯遷往遼東" and was killed the same year.

## Spot checks (all confirmed unless noted)

- **Eighteen Kingdoms:** table rows; "created by military leader Xiang Yu in 206 BCE"; no area, no capitals.
- **Xiang Yu:** "In late 206 BC, Xiang Yu executed Han Cheng ... replaced him with Zheng Chang".
- **Xin of Han:** 205 King of Hán; Yingchuan/Yangzhai; 201 relocation and defection.
- **Chu-Han Contention:** Shen Yang's surrender (205); Zheng Chang replaced by Hán Xin; "In November 205 BCE ... Ying Bu agreed to join Liu Bang"; Tian Shi and Tian An killed.
- **Timeline (206 BC):** Jiaodong, Han Guang, Shen Yang, Hán.
- **Timeline (204 and 202 BC):** 204 Gong Ao dies; 202 Linjiang conquered and Gong Wei executed.
- **Shen Yang:** "In 205 BC, Shen Yang surrendered to Liu Bang and his kingdom became the Henan Commandery".
- **Tian Rong:** the division of Qi; the page itself dates the killings to 205 (the author noted this).
- **Long Ju:** "In late 205 BC ...".
- **Ying Bu:** "Months later Long Ju defeated Ying Bu and conquered Jiujiang"; Huainan 203.
- **Zang Tu:** "killed him at Wuzhong".
- **Han Guang:** "died 206 BC".
- **Gong Ao:** Nan Commandery, Jiangling, died 204.

No event was found mis-dated or missing from its page.

## Cross-dossier routing

- **ea-02-a, kingdom-of-han:** add the gain from henan (205) and the vassal_start for han-2 (205). Take Hán (vassal) and Linjiang out of the han_-203 direct shape.
- **ea-02-a, western-chu:** move the Jiujiang gain to 204 (within one year now). Take Linjiang out of 203 (linjiang stands to 202).
- **ea-02-a, qin-dynasty:** add henan, jiujiang and linjiang to its successors.
- **ea-01, qi:** add a gain from jiaodong (206) and splits to jiaodong and jibei (206).
- **ea-01, yan:** matched (split and gain, 206). The Yan 206 shape lacks the Liaodong Peninsula.
- **ea-02-c:** han-dynasty needs the mirrors for han-2 (201) and linjiang (202). yin should know that Cliopatria's Henan polygon covers Zhaoge and Henei, and that its own polygon sits in southern Hebei.
- **ea-02-x:** huainan (Ying Bu, 203-196) and hengshan (Wu Rui, 206-202).
- **ea-01, minyue:** Cliopatria's Minyue 206 shape holds Nanchang (Yuzhang), which the table gives to Hengshan ("Jiangxi").
