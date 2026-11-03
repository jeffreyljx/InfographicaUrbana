# Review of batch me-05-f (judea, indo-greeks), 2026-10-19

Reviewer: adversarial reviewer, Phase B. Machine copy: history/notes/phase-b/reviews/me-05-f.json.

Validator (--resolve): both valid, no errors. judea: two warnings, tetrarchy-of-galilee-and-peraea and tetrarchy-of-philip are unknown slugs (listed in counterparts_needing_dossiers, accepted). indo-greeks: no warnings. No known-bad Cliopatria rows for either in data/README.md.

## judea: FAIL (back to the author)

Spot checks (all confirmed): /ledger/3 and /ledger/6 (John Hyrcanus: campaign against Samaria 'Beginning in 113 BCE'; 'first conquest was an invasion of the Transjordan in 110 BCE', Medeba taken after a six-month siege); /ledger/8, 11, 12, 14 (Alexander Jannaeus: Gaza 96 BCE; 'From 83 to 80 BCE' Golan, Seleucia, Gamala, Pella, Dium, Gerasa; the twelve cities recovered 'only through negotiations with his elder son, Hyrcanus II'); /ledger/23, 25, 26 (Herod the Great: '22 BCE - Augustus grants Herod the regions of Trachonitis, Batanaea, and Auranitis'; Archelaus ethnarch of Judea, Samaria and Idumea to 6 CE, Antipas Galilee and Peraea to 39, Philip to 34); /ledger/21 (Judea timeline, Caesarea c. 25 BCE replacing Jerusalem as capital). Area: the Judea infobox has no area; acknowledged.

Blocking findings (not applied: they need shape corrections and new events):

1. /keyframe_review/11 (judea_-25) is verdict ok, so -25..-20 draws the full Cliopatria shape: 41 Moab/Edom/Negev cells lost to the Nabataeans at -65 (/ledger/14) and 9 Gerasa-district cells lost at -63 (/ledger/17) come back for six years, and the Hauran added at -22 (/ledger/23) is missing (8 of 45 cells). Make it adjust: minus Moab, Edom, the Negev south of the Beersheba 40 km disc and the Gerasa 40 km disc for -25..-23, and a new keyframe judea_-22 (-22..-20) with the Hauran added.
2. /keyframe_review/12 (judea_-19) keeps the Gerasa 40 km disc (10 cells) lost at -63 with no regain: subtract it too, or source a gain.
3. Missing vassal events. The suzerains carry client events with counterpart judea that have no mirror here: seleucid-empire -134 vassal_start / -129 vassal_end (the John Hyrcanus page confirms the tribute and its end after Antiochus VII's death in 129), roman-republic -63 vassal_start, -40 vassal_end, -37 vassal_start, roman-empire -27 vassal_start, 6 vassal_end. Recording them as rename events does not satisfy the mirror rule or rule 4 (client tint). Add them.
4. /keyframe_review/13 (judea_-4): 16 cells of Herod's kingdom (12 northern Negev around Beersheba, 2 Gaza, 2 Amman) vanish at the partition with no event; Archelaus held Idumea, whose south is the Beersheba country. Add the Negev within 40 km of Beersheba to judea_-4, judea_1 and the dissolve region, or record the loss.
5. /ledger/4 and /ledger/17: counterparts 'Samaria (city and region)' and 'Decapolis (Hellenistic cities)' are not slugs and not listed as needed dossiers; use roman-republic for the Decapolis (cities under the governor of Syria) and nobody or seleucid-empire for Samaria (the page has Antiochus IX sending 6,000 troops to the Samaritans).
6. /keyframe_review/5 vs /ledger/14: judea_-66 keeps the Nabataean cells for -66..-64 while the ledger loses them at -65; move the confidence-1 loss to -63 or cut the keyframe at -65.

Thin (for a gap-filler): /ledger/2 Idumea year (try Idumea); /ledger/9 Moab/Edom/Negev gain, which contradicts the nabataeans dossier's Obodas I regain c. 93 (try Obodas I); /ledger/14 year of the twelve cities' return (try Aretas III); /ledger/22 the post-Actium coastal grants (try Herodian kingdom); /ledger/7 and /ledger/11 previous holders of Galilee and Golan (Itureans? Tigranes? try Ituraea).

## indo-greeks: THIN (valid and honest; ledger short of explanations within a 5-page budget)

Spot checks (all confirmed): /ledger/13 (Indo-Scythians: 'Maues first conquered Gandhara and Taxila ... c. 80 BCE', Taxila 'from Indo-Greek King Apollodotus II'); /ledger/17 ('In 55 BCE, under Azes I, ... victory over Hippostratos'); /ledger/18 ('Rajuvula apparently eliminated Strato II ... c. 10 CE and took Sagala'); /ledger/0, 1, 3 (Indo-Greek Kingdom: Apollodotus I independent c. 180/175; Eucratides 'between ca. 170 BC and 150 BC'; 'from 165 BCE until his death in 130 BCE, Menander I ruled Punjab with Sagala as his capital'). Area: infobox 1,100,000 km2 for 150 BC; no Cliopatria shape in -150; Cliopatria -126 is 784,828 km2 (0.71); the dossier's -165 keyframe is 2,075 cells, about 573,000 km2 at the local cell size (0.52), acknowledged with what is left out.

Keyframes walk cleanly: -175 (902 cells) -> -165 (2,075) by the -165 gain; -> -126 (2,670 after removing Bactria) by the -127 gains and loss; -> -110, -91 by the -110 and -91 losses; -87 adjusted to keep Gandhara/Taxila until the -80 loss; -77 and -55 new keyframes explained by -77/-55 events; -50..9 ok, 9 limited to 10. The stray polygon at 31.5 E in indo-greeks_-31 is flagged by the author.

Ten of 19 events are confidence 1 with the year from Cliopatria: /ledger/2, 6, 7, 8, 9, 10, 11, 12, 15, 16. Pages to try: Menander I, Arachosia (the Indo-Scythians page calls Arachosia Parthian-controlled in Isidore, so the -127 counterpart may be parthian-empire), Heliocles I, Hermaeus, Sakastan, Mathura (Indo-Greek control 'between 185 BCE and 85 BCE', so the -91 loss is six years early), Maues.

## Cross-dossier matrix (routing)

Matched: judea found -142 / seleucid -143 loss; judea -126 / seleucid -126; indo-greeks -127 gain / greco-bactrian -127 dissolve; -91 / shunga -91; -80 / indo-scythians -80; -78 / indo-scythians -77; dissolve 10 / indo-scythians 10.

Missing in the counterpart (route to its group): seleucid-empire (me-05) has no loss for judea -141 (Acra), -103 (Galilee), -80 (Golan); nabataeans (me-05) none for judea -110 (Medeba), -91, -80 (Gerasa), -65; roman-republic (eu-03) none for the -63 coastal plain; roman-empire (eu-04) none for -25 (coast) or -22 (Hauran); greco-bactrian-kingdom (me-05) none for indo-greeks -150 (Gandhara); yuezhi (ia-01) none for indo-greeks -110 and -80; indo-scythians (sa-02) none for indo-greeks -77 (Taxila).

Mismatches (both sides exist and disagree): nabataeans -96 loss / -93 regain of Moab and Gilead vs judea -91 gain / -65 loss of Moab, Edom, Negev; nabataeans -144 loss of Gilead to judea vs judea's ex-Seleucid founding land; seleucid -91 loss to judea vs judea gains at -103 and -80; roman-empire 6 gain takes the whole Cliopatria Judea shape while judea's dissolve gives only Judea, Samaria, Idumea and Caesarea; greco-bactrian -180 gain and -170 gain from indo-greeks vs indo-greeks' found -175 and contest -170 (double-drawn 175-150); indo-scythians -110 gain from nobody vs indo-greeks -110 and -127 losses to indo-scythians; indo-scythians -88 gain from indo-greeks with no indo-greeks loss (and the reviewer found no 'around 88 B.C.' sentence on the Indo-Scythians page); indo-scythians -50 loss of the eastern Punjab to indo-greeks vs indo-greeks' -55 loss of the western Punjab, with neither mirrored.

Exceptions: the two tetrarchies (listed as needed dossiers); parthian-empire (me-06, not run) for Antigonus 40-37; counterpart nobody events.
