"use client";
import { useEffect, useRef, useState } from "react";

/**
 * A guide's demo clip: a short silent loop recorded from the map (scripts/guide/capture.mjs). It plays while it is on
 * screen and pauses off it; a click or the button pauses and plays it. With reduced motion asked for, it waits on its
 * first frame until played.
 */
export default function GuideVideo({ src, poster, w, h, label }: { src: string; poster: string; w: number; h: number; label: string }) {
  const ref = useRef<HTMLVideoElement>(null);
  const held = useRef(false);   // paused by the visitor (or by reduced motion): don't restart it on scroll
  const [paused, setPaused] = useState(true);

  useEffect(() => {
    const v = ref.current;
    if (!v) return;
    if (window.matchMedia?.("(prefers-reduced-motion: reduce)").matches) held.current = true;
    if (typeof IntersectionObserver === "undefined") { if (!held.current) v.play().catch(() => {}); return; }
    const io = new IntersectionObserver(([e]) => {
      if (e.isIntersecting && !held.current) v.play().catch(() => {});
      else if (!e.isIntersecting) v.pause();
    }, { threshold: 0.4 });
    io.observe(v);
    return () => io.disconnect();
  }, []);

  const toggle = () => {
    const v = ref.current;
    if (!v) return;
    if (v.paused) { held.current = false; v.play().catch(() => {}); } else { held.current = true; v.pause(); }
  };

  return (
    <div className="g-video">
      <video ref={ref} muted loop playsInline preload="metadata" poster={poster} width={w} height={h} aria-label={label}
        onClick={toggle} onPlay={() => setPaused(false)} onPause={() => setPaused(true)}>
        <source src={src} type="video/mp4" />
      </video>
      <button type="button" className="g-play" onClick={toggle} aria-label={paused ? "Play the demo" : "Pause the demo"}>
        <svg width="14" height="14" viewBox="0 0 16 16" aria-hidden="true">
          {paused ? <path d="M4.5 2.2v11.6L13.6 8z" fill="currentColor" /> : <path d="M4 2.5h3v11H4zM9 2.5h3v11H9z" fill="currentColor" />}
        </svg>
      </button>
    </div>
  );
}
