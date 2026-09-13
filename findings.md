л# Findings — Extended Analysis

## 1. UCDP Verification (12 incidents)
12 incidents—documented and verified by the UCDP. The verification of these incidents is based on media reports and UN reports, as most incidents in the conflict remain unverified due to information noise and MINURSO’s inability to travel to the sites to investigate. Therefore, based on these 12 entries, it is not possible to track trends over time or determine when the conflict was more active and when it was calmer.

Translated with DeepL.com (free version)

The established tolerance for matching events against GDELT was a window of ±2 days.[^1]

[^1]: See the Limitations section of the README for why this window was chosen (illustrated by the Guerguerat case, where the incident occurred on the 13th and the article appeared on the 14th–15th).

**1. Clashes in Guerguerat (13–14.11.2020)**
The incident began when Moroccan forces entered Guerguerat to disperse protesters and break the road blockade (November 13). According to a source citing POLISARIO and the Western Sahara army, shelling occurred a day or two later, allegedly killing 2 Moroccan soldiers.
Casualties: 2 (Morocco) — best: 2, high: 2 · Source: [Atalayar](https://atalayar.com/en/articulo/politics/polisario-front-claims-have-caused-deaths-against-moroccan-army/20201115103713148419.html)

**2. Shelling of Moroccan Army Garrison near Ouarkziz (08.02.2021)**
POLISARIO carried out an attack on a Moroccan armed forces garrison. According to POLISARIO's statements, 3 Moroccan soldiers were killed; Morocco's Prime Minister publicly called this a "media war."
Casualties: 0–3 (Morocco, disputed) — best: 0, high: 3 · Source: [Bladi.net](https://www.bladi.net/polisario-militaires-marocains,79643.html)

**3. Shelling of Moroccan Forces near Touizgui (the Berm) (21.02.2021)**
The Ministry of Defense of the Sahrawi Arab Democratic Republic (POLISARIO Front) announced large-scale attacks on Moroccan forces near the sand wall ("Wall of Shame"). In response, Morocco subsequently began actively using drones.
Casualties: 0–5 (Morocco, unconfirmed) — best: 0, high: 5 · Source: [North Africa Post](https://north-africa.com/western-sahara-tensions-running-high-as-polisario-front-says-three-moroccan-soldiers-killed-in-attack-in-touizgui/)

**4. Drone Strike Kills Head of POLISARIO Gendarmerie (06.04.2021)**
The head of the POLISARIO gendarmerie was killed by a drone strike on April 6, 2021 — considered one of the first documented uses of drones by Morocco in this conflict.
Casualties: 3 (POLISARIO) — best: 3, high: 3 · Source: AFP / Jeune Afrique; UN Secretary-General report S/2021/843

**5. Shelling of Algerian Drivers (01.11.2021)**
According to Algeria, a Moroccan strike in the border area between Mauritania and Western Sahara killed 3 civilian drivers.
Casualties: 3 (Civilians) — best: 3, high: 3 · Source: [Reuters](https://www.reuters.com/world/algeria-says-moroccan-bombardment-killed-three-algerians-western-sahara-border-2021-11-03/)

**6. Mijek: Accusation of Civilian Shelling (14.11.2021)**
The POLISARIO Front accused Moroccan armed forces of killing 11 civilians in drone strikes on November 14–15 in the Mijek area, controlled by POLISARIO. The event may be linked to the upcoming UN vote on the mission's mandate in the region.
Casualties: 0–11 (Civilians, alleged) — best: 0, high: 11 · Source: CrisisGroup – CrisisWatch (November 2021)

**7. Mauritanian Gold Prospectors (03.01.2022)**
CrisisWatch (January 2022) reported that a Moroccan drone strike on January 3 killed three Mauritanian civilians in the UN buffer zone.
Casualties: 3 (Civilians) — best: 3, high: 3 · Source: CrisisGroup – CrisisWatch (January 2022)

**8. Drone Strike on the Mehaires Area (10.01.2022)**
Sources close to the Saharawi peace movement reported in mid-January that a drone strike killed four POLISARIO members in the eastern Mehaires area, controlled by POLISARIO.
Casualties: 4 (POLISARIO) — best: 4, high: 4 · Source: CrisisGroup – CrisisWatch (January 2022)

**9. Airstrike on a Truck (10.04.2022)**
Media affiliated with the POLISARIO independence movement reported that a Moroccan airstrike hit trucks near the border between the disputed territory and Mauritania early Sunday morning, killing three people of unknown nationality.
Casualties: 3 (Unidentified) — best: 3, high: 3 · Source: [The New Arab](https://www.newarab.com/news/algeria-accuses-morocco-killing-3-edge-w-sahara)

**10. Clashes Along the Berm (15.11.2022)**
According to MINURSO reports, Moroccan forces used aircraft and artillery to repeatedly strike POLISARIO forces attempting to cross the wall at various points.
Casualties: 4 (POLISARIO) — best: 4, high: 4 · Source: UN reports (indirect)

**11. Explosions in Smara (29.10.2023)**
Four explosions occurred in Smara, killing one young man and wounding three others, two critically. The blast struck three residential neighborhoods and was not directed at military positions. POLISARIO claimed responsibility through its press office.
Casualties: 1 (Unidentified) — best: 1, high: 1 · Source: [Washington Institute](https://www.washingtoninstitute.org/policy-analysis/polisario-attack-smara-worrying-escalation-morocco)

**12. Strike on POLISARIO in Al-Hauza (18.01.2025)**
Moroccan media reported a strike on the POLISARIO Front, as reflected in the CrisisWatch report for January 2025.
Casualties: 3 (POLISARIO) — best: 3, high: 3 · Source: CrisisGroup – CrisisWatch (January 2025)

---

## 2. GDELT Error Catalog (6 types)

**1. Historical reference presented as a current event.** An event with CAMEO code 203 (ethnic cleansing, dated 28.07.2026) appeared in `conflicts`. On examining the source referenced by GDELT, it turned out to be unrelated to any 2026 event — the article was actually about phosphate deposits and the US, with a historical reference to 1979. In addition, the event's actor — LIBERATION ARMY — did not match the actor discussed in the article — Morocco.

**2. Geographic homonymy.** GDELT confused Western Sahara with the "Western Desert of Egypt" — the region's name is a homonym of an Arabic phrase — picking up an event about the elimination of militants in the Egyptian desert by internal security forces. On top of that, the event itself took place back in 2017.

**3. Irrelevant content passing the filter.** An event was categorized as conflict-related (Goldstein values from -9 to -10 count as military violence), but the article turned out to be about Christopher Nolan's film "The Odyssey," filmed in the region.

**4. Future event presented as fact.** A news article about a planned diplomatic meeting in February 2026 was tagged with code 57 (as an already-signed agreement).

**5. Extraction of a secondary actor.** The `conflicts` table contains events related to the break in relations between Algeria and Morocco in August 2021. Israel appeared in the columns showing who was involved — which has no relation to the rupture between the two countries. Possibly connected to an Israeli minister's visit to Morocco in the same period; GDELT latched onto parallel contexts and events.

**6. Absence of drone-specific codes.** Based on UN data and CrisisWatch reports, Morocco primarily uses drones against POLISARIO. GDELT's CAMEO codes include specific codes for drone strikes (the 195x series). However, on checking, it turned out they are almost never used in `conflicts`.

---

## 3. Share of UCDP-Confirmed Events by Month

The share of events from `conflicts` that found a match in the UCDP table stays within a range of 0.10–0.34 by month. This indicates that GDELT accumulates media mentions of situations in the selected region through machine filters, bypassing any confirmation stage, while UCDP collects acts of violence and releases them only after confirmation — pointing to a different structure of information sources.

The only exception is October 2023, with a match rate of 0.71. This does not mean the data can be relied upon here — there were only 7 events that month, so a few matches against such a small total produce a spike in the share; it only indicates statistical noise.
