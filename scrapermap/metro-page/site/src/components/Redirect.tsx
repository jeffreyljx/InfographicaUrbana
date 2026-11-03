"use client";
import { useEffect } from "react";
/** Client-side redirect that keeps the query string (e.g. ?sort=pipeline&order=asc). */
export default function Redirect({ to }: { to: string }) {
  useEffect(() => { location.replace(to + location.search + location.hash); }, [to]);
  return null;
}
