# Protokoll‑täckningsmatris (Protocol Coverage Matrix)

Detta dokument beskriver **hur axis_doc_tool förhåller sig till de officiella protokollen**:

* **Protokoll – Enskild Kamera**
* **Protokoll – Anläggning**

Syftet är **inte** styrning eller policy, utan ett praktiskt stöd för tekniker:

* Vad kan verktyget leverera automatiskt?
* Vad kräver fortfarande manuell kontroll eller signering?

---

## Förklaringar

**Källa** anger hur informationen tas fram:

* **Automatisk (Axis API)** – Hämtas direkt från kameran
* **Manuell (Tekniker – inmatning)** – Teknikern skriver in uppgiften i verktyget
* **Manuell (Fysisk kontroll)** – Kräver fysisk/visuell verifiering på plats
* **Ej hanterat av verktyg** – Utanför verktygets scope

---

# 1. Protokoll – Enskild Kamera

| Protokollrad                         | Verktygsfält                  | Källa                          | Kommentar                                |
| ------------------------------------ | ----------------------------- | ------------------------------ | ---------------------------------------- |
| Upptagningsområde enligt beställning | Riktning / Vybeskrivning      | Manuell (Tekniker – inmatning) | Fri text, kompletterar bildinställningar |
| Focus                                | Fokusläge / Autofokusstatus   | Automatisk (Axis API)          | Visuell kvalitet verifieras manuellt     |
| PTZ                                  | PTZ-stöd + status             | Automatisk (Axis API)          | Gäller endast PTZ-modeller               |
| Preset                               | PTZ-presets (namn + antal)    | Automatisk (Axis API)          | Innehåll verifieras manuellt             |
| Motion detect                        | Rörelsedetektering aktiv      | Automatisk (Axis API)          | Konfiguration, ej funktionstest          |
| Motion detect maskning               | Masker (antal + namn)         | Automatisk (Axis API)          | Placering verifieras manuellt            |
| Upplösning & komprimering            | Streamprofiler                | Automatisk (Axis API)          | Codec, upplösning, FPS                   |
| Nätverksåtkomst                      | IP, subnet, gateway, tjänster | Automatisk (Axis API)          |                                          |
| Bildkvalitet dagtid                  | Bildinställningar dag         | Automatisk (Axis API)          | Bedömning ej automatiserad               |
| Bildkvalitet nattetid                | Bildinställningar natt/IR     | Automatisk (Axis API)          | Kräver visuell kontroll                  |
| Testbild sparad                      | –                             | Ej hanterat av verktyg         | Manuell åtgärd                           |
| Rengöring lins och kapsling          | –                             | Ej hanterat av verktyg         | Fysisk åtgärd                            |
| Kundunik extradekal monterad         | –                             | Ej hanterat av verktyg         | Fysisk åtgärd                            |
| Camera Tampering                     | Tampering aktiv + nivå        | Automatisk (Axis API)          | Funktionstest manuellt                   |
| Test av I/O‑modul                    | I/O konfigurerad              | Automatisk (Axis API)          | Test ej automatiserat                    |

---

# 2. Protokoll – Anläggning

| Protokollrad                                 | Verktygsfält                      | Källa                                | Kommentar               |
| -------------------------------------------- | --------------------------------- | ------------------------------------ | ----------------------- |
| Egenkontroll enskild kamera                  | Kamera‑rapport genererad          | Automatisk (Verktyg)                 | Sammanfattar kameradata |
| DVR konfigurerad                             | Inspelningsinställningar (kamera) | Automatisk (Axis API)                | VMS‑sida ej täckt       |
| Batteridelar ifylld och fastsatt             | –                                 | Ej hanterat av verktyg               | Fysisk installation     |
| Systemet testat på batteribackup             | –                                 | Ej hanterat av verktyg               | Funktionstest           |
| Visuell maskning                             | Privacy masks                     | Automatisk (Axis API)                | Visuell kontroll krävs  |
| Motion detect                                | Rörelsedetektering                | Automatisk (Axis API)                |                         |
| Motion detect maskning                       | Masker                            | Automatisk (Axis API)                |                         |
| Upplösning & komprimering                    | Streamprofiler                    | Automatisk (Axis API)                |                         |
| Nätverksåtkomst                              | IP, subnet, gateway, VLAN         | Automatisk (Axis API + manuell VLAN) |                         |
| Ingångar – Triggeringar                      | I/O‑ingångar                      | Automatisk (Axis API)                | Funktionstest manuellt  |
| Utgångar – Styrningar                        | I/O‑utgångar                      | Automatisk (Axis API)                | Funktionstest manuellt  |
| Preset‑lägen programmerade                   | PTZ‑presets                       | Automatisk (Axis API)                |                         |
| Scheman                                      | Schema existerar                  | Automatisk (Axis API)                | Innehåll ej verifierat  |
| Klockan ställd                               | NTP + tidssynk                    | Automatisk (Axis API)                |                         |
| Programmerat enligt beställning              | Sammanfattning inställningar      | Delvis automatisk                    | Tolkning manuell        |
| Anläggning kontrollerad mot behovsanalys     | –                                 | Ej hanterat av verktyg               | Bedömningspunkt         |
| Urplockning av inspelat material             | –                                 | Ej hanterat av verktyg               | Funktionstest           |
| Samtlig dokumentation kontrollerad/reviderad | Dokument genererade               | Automatisk (Verktyg)                 |                         |
| Utbildning av slutanvändare                  | –                                 | Ej hanterat av verktyg               | Administrativt          |
| Manual överlämnad                            | –                                 | Ej hanterat av verktyg               | Administrativt          |
| Kameraskyltar monterade                      | –                                 | Ej hanterat av verktyg               | Fysisk åtgärd           |
| Nycklar återlämnade                          | –                                 | Ej hanterat av verktyg               | Administrativt          |
| Städning utförd                              | –                                 | Ej hanterat av verktyg               | Fysisk åtgärd           |

---

## Sammanfattning

* **axis_doc_tool täcker alla tekniskt verifierbara punkter** i båda protokollen
* Verktyget gör **inga påståenden om fysisk, visuell eller administrativ kontroll**
* Verktygets rapport används som **underlag (metadata)** för ifyllnad och signering
* Slutligt ansvar och signatur ligger alltid hos tekniker

---

*Detta dokument är avsett som internt stöd för tekniker och utveckling av axis_doc_tool.*

