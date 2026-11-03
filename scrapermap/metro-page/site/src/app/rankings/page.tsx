import type { Metadata } from "next";
import Redirect from "@/components/Redirect";
export const metadata: Metadata = { title: "Districts", robots: { index: false }, alternates: { canonical: "/districts/" } };

/** The districts league table moved from /rankings/ to /districts/ (27 Sep 2026); this keeps old links working on a static host. */
export default function RankingsMoved() {
  return (
    <>
      <meta httpEquiv="refresh" content="0; url=/districts/" />
      <Redirect to="/districts/" />
      <main className="page"><p>The district rankings are now at <a href="/districts/">/districts/</a>.</p></main>
    </>
  );
}
