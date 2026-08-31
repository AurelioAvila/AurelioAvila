## Aurelio Avila

I build Windows software and security tooling, and I work as an incident responder.

Most of what is here falls into two halves that keep feeding each other. On one
side, shipped products: desktop applications people install, review and complain
about, distributed through the Microsoft Store, winget and the usual software
catalogues. On the other, security engineering: detection rules, forensic
tooling and incident write-ups, each built to be run and checked rather than
read and believed.

Working both sides changes how you build. Handling alerts for a living teaches
you what an attacker actually does before your product's threat model is
finished, and shipping to strangers teaches you that a control nobody can
understand is a control nobody uses.

---

### Products

<table>
<tr>
<td width="50%" valign="top">

**[PC Tweaker](https://github.com/AurelioAvila/pc-tweaker-app)**

Windows performance, gaming, privacy and maintenance tuning where every change
is snapshotted before it is applied, so any tweak can be reversed.

[![Downloads](https://img.shields.io/github/downloads/AurelioAvila/pc-tweaker-app/total?style=flat-square&label=downloads&color=2E7D32)](https://github.com/AurelioAvila/pc-tweaker-app/releases)
[![Release](https://img.shields.io/github/v/release/AurelioAvila/pc-tweaker-app?style=flat-square&label=release&color=0078D4)](https://github.com/AurelioAvila/pc-tweaker-app/releases)

[Microsoft Store](https://apps.microsoft.com/detail/9nh3c6dt1g87) · Softpedia
review 4.5/5 · [MajorGeeks](https://www.majorgeeks.com/files/details/pc_tweaker.html) 5.0/5

</td>
<td width="50%" valign="top">

**[Glarion](https://github.com/AurelioAvila/glarion)**

Website security scanning for agencies. No scan runs against a domain whose
ownership has not been proved, and the proof is rechecked when the scan
executes, not when it is queued.

[![Tests](https://img.shields.io/badge/tests-208-52C78D?style=flat-square)](https://github.com/AurelioAvila/glarion)
[![Rust](https://img.shields.io/badge/Rust%20%2B%20Axum-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/AurelioAvila/glarion)

[Read the security model](https://github.com/AurelioAvila/glarion#the-constraint-everything-else-is-arranged-around)

</td>
</tr>
<tr>
<td width="50%" valign="top">

**[Redaxa](https://github.com/AurelioAvila/redaxa)**

Catches secrets, credentials and personal data in text before it is pasted into
ChatGPT, Claude, Gemini or Copilot. Detection runs locally.

[![Release](https://img.shields.io/github/v/release/AurelioAvila/redaxa?style=flat-square&label=release&color=7C3AED)](https://github.com/AurelioAvila/redaxa/releases)

Desktop app, browser extension and web version

</td>
<td width="50%" valign="top">

**[Social Dashboard](https://github.com/AurelioAvila/social-dashboard)**

Local-first analytics for YouTube, Instagram, TikTok and X. Credentials and
history stay on the machine; nothing is relayed through a server of mine.

[![Release](https://img.shields.io/github/v/release/AurelioAvila/social-dashboard?style=flat-square&label=release&color=0078D4)](https://github.com/AurelioAvila/social-dashboard/releases)

[Product site](https://socialdashboard.getcertsprint.com/)

</td>
</tr>
</table>

---

### Security engineering

Each of these is a working tool with its own test suite, not a write-up of
something that was done once. Detection logic is validated against samples that
should fire and samples that should not, and the validation runs in CI.

| Project | What it does |
| --- | --- |
| **[detection-engineering-rules](https://github.com/AurelioAvila/detection-engineering-rules)** | YARA and Sigma rules, each checked against true and false positive cases. Sigma is compiled to real Splunk SPL with pySigma rather than validated as YAML. |
| **[network-traffic-analysis](https://github.com/AurelioAvila/network-traffic-analysis)** | Scapy PCAP analyser for port scans, C2 beaconing and floods. A statistical baseline catches slow floods that fixed thresholds structurally cannot, with a side-by-side demo showing the difference. |
| **[malware-triage-hash](https://github.com/AurelioAvila/malware-triage-hash)** | Hash reputation joined to behavioural scoring, so an unknown sample is not read as a clean one. Ships a Sentinel KQL hunt. |
| **[ransomware-dfir-timeline](https://github.com/AurelioAvila/ransomware-dfir-timeline)** | Process, Prefetch, Registry and filesystem artifacts correlated into a single timeline, from the opened attachment to mass encryption, with root cause and detection gaps. |
| **[phishing-email-analysis](https://github.com/AurelioAvila/phishing-email-analysis)** | Parses raw `.eml`, extracts headers, URLs and attachment hashes, flags typosquatting and urgency patterns, enriches through VirusTotal. |
| **[splunk-brute-force-detection](https://github.com/AurelioAvila/splunk-brute-force-detection)** | SPL detections for brute force and password spraying in Windows Security logs, with threshold tuning notes and a triage playbook. |
| **[soc-home-lab](https://github.com/AurelioAvila/soc-home-lab)** | Wazuh and OpenSearch lab: custom rules, agent deployment, ingestion validation, and the full path from alert to incident report. |
| **[dma-guide](https://github.com/AurelioAvila/dma-guide)** | Reference on DMA attack mechanics and the controls that stop them, from IOMMU and VT-d to Kernel DMA Protection. |

Everything is mapped to MITRE ATT&CK and, where behaviour matters more than a
screenshot, reproducible from the repository.

---

### Background

SOC analyst, currently Tier 1, handling alert triage, log correlation and
detection tuning across Microsoft Sentinel, Splunk and Wazuh. Before the
products there was the day job, and the day job is why the products are built
the way they are.

**Certifications**

[![Security+](https://img.shields.io/badge/CompTIA-Security%2B-C8202F?style=flat-square&logo=comptia&logoColor=white)](https://www.comptia.org/certifications/security)
[![CySA+](https://img.shields.io/badge/CompTIA-CySA%2B-C8202F?style=flat-square&logo=comptia&logoColor=white)](https://www.comptia.org/certifications/cybersecurity-analyst)
[![SC-200](https://img.shields.io/badge/Microsoft-SC--200-0078D4?style=flat-square&logo=microsoft&logoColor=white)](https://learn.microsoft.com/certifications/security-operations-analyst/)
[![BTL1](https://img.shields.io/badge/Security_Blue_Team-BTL1-1E90FF?style=flat-square)](https://www.securityblue.team/)
[![Trinity ISE III](https://img.shields.io/badge/Trinity_ISE_III-English_C1-2E8B57?style=flat-square)](https://www.trinitycollege.com/)
[![Anthropic Introduction to MCP](https://img.shields.io/badge/Anthropic-Introduction_to_MCP-D97757?style=flat-square&logo=anthropic&logoColor=white)](https://verify.skilljar.com/c/3eprxfyv4fir)
[![Anthropic AI Capabilities and Limitations](https://img.shields.io/badge/Anthropic-AI_Capabilities_%26_Limitations-D97757?style=flat-square&logo=anthropic&logoColor=white)](https://academy.claude.com/verify/acfb15b8c0f1ef56579439e208961368)
[![Anthropic AI Fluency for Builders](https://img.shields.io/badge/Anthropic-AI_Fluency_for_Builders-D97757?style=flat-square&logo=anthropic&logoColor=white)](https://academy.claude.com/verify/a21f60f4e2670aefaf0ec8cd78595c38)

**Tools I reach for**

Rust and Tauri for anything that has to touch Windows properly. TypeScript and
React on top of it. Python for analysis. KQL and SPL for hunting. Postgres when
state has to survive.

**Languages** — Italian (native), English (C1), French (B2), Spanish (B1)

---

### Contact

Open to security engineering work and to conversations about the products above.

**[aurelio_11@outlook.it](mailto:aurelio_11@outlook.it)** · Amsterdam
