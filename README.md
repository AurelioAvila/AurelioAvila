# Aurelio Avila

Security operations, detection engineering and Windows software.

I build defensive tools and practical applications, with a focus on clear
evidence, useful diagnostics and understandable controls. My work spans
incident investigation, reproducible security labs and products for creators,
digital agencies and Windows users.

[Explore products](#products) · [Security projects](#security-engineering) ·
[Skills and tools](#skills-and-tools) · [Get in touch](#contact)

---

### Products

<table>
<tr>
<td width="50%" valign="top">

**[Glarion](https://github.com/AurelioAvila/glarion)**

Website security monitoring and client-ready reporting for digital agencies.
Glarion identifies meaningful changes, turns technical findings into clear
deliverables and requires current proof of domain control before active scans.

[![CI](https://img.shields.io/github/actions/workflow/status/AurelioAvila/glarion/ci.yml?style=flat-square&label=CI&color=52C78D)](https://github.com/AurelioAvila/glarion/actions/workflows/ci.yml)
[![Rust](https://img.shields.io/badge/Rust%20%2B%20Axum-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/AurelioAvila/glarion)

[Product site and current plans](https://glarion.app/)

[Check a website without an account](https://glarion.app/#public-check) ·
[View the sample report](https://glarion.app/sample-report.html) ·
[Read the security model](https://github.com/AurelioAvila/glarion#the-constraint-everything-else-is-arranged-around)

</td>
<td width="50%" valign="top">

**[PC Tweaker](https://github.com/AurelioAvila/pc-tweaker-app)**

Windows performance, gaming, privacy and maintenance tools with reversible
tweaks and recovery features. Review each action and its requirements before
applying system changes.

[![GitHub downloads](https://img.shields.io/github/downloads/AurelioAvila/pc-tweaker-app/total?style=flat-square&label=GitHub%20Releases&color=2563EB)](https://github.com/AurelioAvila/pc-tweaker-app/releases)
[![Release](https://img.shields.io/github/v/release/AurelioAvila/pc-tweaker-app?style=flat-square&label=release&color=0078D4)](https://github.com/AurelioAvila/pc-tweaker-app/releases)

[Product site](https://pctweaker.app/) ·
[Microsoft Store](https://apps.microsoft.com/detail/9nh3c6dt1g87) ·
[Softpedia](https://www.softpedia.com/get/Tweak/System-Tweak/Avila-PC-Tweaker.shtml) ·
[MajorGeeks](https://www.majorgeeks.com/files/details/pc_tweaker.html)

</td>
</tr>
<tr>
<td width="50%" valign="top">

**[Redaxa](https://github.com/AurelioAvila/redaxa)**

Catches secrets, credentials and personal data in text before it is pasted into
ChatGPT, Claude, Gemini or Copilot. Scanned on our backend, never sent to an AI
provider — details in the [privacy section](https://github.com/AurelioAvila/redaxa#privacy).

[![Release](https://img.shields.io/github/v/release/AurelioAvila/redaxa?style=flat-square&label=release&color=7C3AED)](https://github.com/AurelioAvila/redaxa/releases)

Desktop app, browser extension and web version

[Try the web app](https://promptshield-beta.vercel.app/) ·
[Download for Windows](https://github.com/AurelioAvila/redaxa/releases/latest)

</td>
<td width="50%" valign="top">

**[Redexa Social](https://github.com/AurelioAvila/redexa-social)**

Local-first creator analytics for YouTube, Instagram, TikTok and X, subject to
platform permissions and API availability. Analytics history stays on your
device. Account connections and optional paid features use the services
described in the [privacy policy](https://redexa.getcertsprint.com/privacy).

[![Release](https://img.shields.io/github/v/release/AurelioAvila/redexa-social?style=flat-square&label=release&color=0078D4)](https://github.com/AurelioAvila/redexa-social/releases)

[Product site](https://redexa.getcertsprint.com/) ·
[Download for Windows](https://github.com/AurelioAvila/redexa-social/releases/latest)

</td>
</tr>
<tr>
<td colspan="2" valign="top">

**[CertSprint](https://getcertsprint.com/)**

Practice tests for IT certification exam prep (Security+, CySA+ and other
vendor tracks), built to mirror real exam format and scoring.

</td>
</tr>
</table>

---

### Security engineering

Explore detection tools, investigation walkthroughs and documented labs.
Repository READMEs explain the available evidence, sample data, test commands
and limitations so you can evaluate each project directly.

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

The incident and detection projects include MITRE ATT&CK context where applicable.

---

### Background

SOC analyst, currently Tier 1, handling alert triage, log correlation and
detection tuning across Microsoft Sentinel, Splunk and Wazuh.

**Certifications and course credentials**

[![Security+](https://img.shields.io/badge/CompTIA-Security%2B-C8202F?style=flat-square&logo=comptia&logoColor=white)](https://www.comptia.org/certifications/security)
[![CySA+](https://img.shields.io/badge/CompTIA-CySA%2B-C8202F?style=flat-square&logo=comptia&logoColor=white)](https://www.comptia.org/certifications/cybersecurity-analyst)
[![SC-200](https://img.shields.io/badge/Microsoft-SC--200-0078D4?style=flat-square&logo=microsoft&logoColor=white)](https://learn.microsoft.com/certifications/security-operations-analyst/)
[![BTL1](https://img.shields.io/badge/Security_Blue_Team-BTL1-1E90FF?style=flat-square)](https://www.securityblue.team/)
[![Trinity ISE III](https://img.shields.io/badge/Trinity_ISE_III-English_C1-2E8B57?style=flat-square)](https://www.trinitycollege.com/)
[![Anthropic Introduction to MCP](https://img.shields.io/badge/Anthropic-Introduction_to_MCP-D97757?style=flat-square&logo=anthropic&logoColor=white)](https://verify.skilljar.com/c/3eprxfyv4fir)
[![Anthropic AI Capabilities and Limitations](https://img.shields.io/badge/Anthropic-AI_Capabilities_%26_Limitations-D97757?style=flat-square&logo=anthropic&logoColor=white)](https://academy.claude.com/verify/acfb15b8c0f1ef56579439e208961368)
[![Anthropic AI Fluency for Builders](https://img.shields.io/badge/Anthropic-AI_Fluency_for_Builders-D97757?style=flat-square&logo=anthropic&logoColor=white)](https://academy.claude.com/verify/a21f60f4e2670aefaf0ec8cd78595c38)

### Skills and tools

| Area | Skills, platforms and tools |
| --- | --- |
| **Security operations** | Alert triage · Incident investigation · Log correlation · Threat hunting · Detection tuning · Escalation and incident reporting · SOAR playbooks |
| **SIEM and detection** | Microsoft Sentinel · KQL · Splunk · SPL · Wazuh · OpenSearch · Sigma · YARA · pySigma · MITRE ATT&CK |
| **DFIR and malware analysis** | Windows event analysis · Process, Prefetch, Registry and filesystem artifacts · Timeline reconstruction · Hash reputation · Behavioural triage · VirusTotal API · Sandbox evidence |
| **Network and email security** | Wireshark · Scapy · PCAP analysis · Traffic baselining · Port-scan, beaconing and flood detection · Email header analysis · IOC extraction and enrichment |
| **Application and AI security** | Nuclei · SSRF protection · Domain ownership verification · Secret and PII detection · Data-loss prevention · LLM security · MCP fundamentals |
| **Software development** | Rust · TypeScript · Python · JavaScript · SQL · React · Tauri · FastAPI · Axum · PostgreSQL · REST APIs |
| **Platforms and identity** | Windows 10/11 · Linux and Ubuntu · Microsoft Azure · Microsoft Entra ID · Microsoft Store · winget |
| **Engineering workflow** | Git · GitHub · GitHub Actions · CI/CD · Automated testing · Visual Studio Code · Security scanning · Release automation |
| **Threat-intelligence frameworks** | STIX/TAXII · Pyramid of Pain · IOC lifecycle · Behaviour-to-technique mapping |

The technologies above are reflected in shipped products, reproducible security
labs or day-to-day security operations.

**Languages** — Italian (native), English (C1), French (B2), Spanish (B1)

---

### Contact

**[aurelio_11@outlook.it](mailto:aurelio_11@outlook.it)** · Amsterdam

Happy to talk about any of the products above, and open to security
engineering work.
