# UCP Estimation Guide — IT3120 OOAD

Use Case Point (UCP) method for estimating project size and effort.
Reference: Karner (1993), as taught in IT3120.

---

## Formula

```
UCP = UUCP × TCF × EF

UUCP = UAW + UUCW
Effort (hours) = UCP × PHM
```

---

## Step 1: UAW — Unadjusted Actor Weight

Classify each actor and sum weights.

| Actor Type | Description | Weight |
|-----------|-------------|--------|
| Simple | External system interacting via well-defined API | 1 |
| Medium | External system using protocol or text-based interface | 2 |
| Complex | Human interacting through GUI | 3 |

**Rules**:
- Each distinct actor type counted once (not each instance)
- "System" actors (automated internal subsystems that represent external interfaces) = Simple
- Mobile app users, web users = Complex (GUI)
- Batch jobs, timers = Simple

**Example (Ricons)**:
| Actor | Type | Weight |
|-------|------|--------|
| Hệ thống phân công (API) | Simple | 1 |
| Hệ thống theo dõi (API) | Simple | 1 |
| Hệ thống thanh toán (API) | Simple | 1 |
| Khách hàng (mobile/web GUI) | Complex | 3 |
| Tài xế giao hàng (mobile GUI) | Complex | 3 |
| **UAW** | | **9** |

---

## Step 2: UUCW — Unadjusted Use Case Weight

Classify each UC by number of transactions and sum weights.

| UC Type | Transactions | Weight |
|---------|-------------|--------|
| Simple | 1–3 | 5 |
| Medium | 4–7 | 10 |
| Complex | > 7 | 15 |

**"Transaction" definition**: A step/interaction between actor and system that is atomic (either completes fully or rolls back). Typically = one numbered step in the main flow that involves the system.

**Example (Ricons)**:
| UC | Main Flow Steps | Type | Weight |
|----|----------------|------|--------|
| UC-01: Đặt đơn hàng | 4 | Simple | 5 |
| UC-02: Phân công giao hàng | 6 | Medium | 10 |
| UC-03: Vận chuyển đơn hàng | 13 | Complex | 15 |
| UC-04: Xác nhận giao hàng | 5 | Medium | 10 |
| UC-05: Thanh toán | 5 | Medium | 10 |
| **UUCW** | | | **50** |

**UUCP = UAW + UUCW = 9 + 50 = 59**

---

## Step 3: TCF — Technical Complexity Factor

Rate each technical factor T1–T13 from 0–5.

```
TFactor = Σ(Ti × Wi)
TCF = 0.6 + (0.01 × TFactor)
```

| Factor | Description | Weight | 0 → 5 scale |
|--------|-------------|--------|-------------|
| T1 | Distributed system | 2 | 0=all local, 5=must run on optimal node per situation |
| T2 | Response time / performance | 1 | 0=no special req, 5=perf tools required at design+dev+deploy |
| T3 | End-user efficiency | 1 | 0=no special req, 5=need tools to demonstrate efficiency goals |
| T4 | Complex internal processing | 1 | 0–5 = number of: security/crypto, broad logic, broad math, many exceptions, complex I/O |
| T5 | Reusable code | 1 | 0=not considered, 5=packaged+documented+user-configurable via params |
| T6 | Easy installation | 0.5 | 0=no special req, 5=complex data migration + auto install tools needed |
| T7 | Easy to operate | 0.5 | 0=standard backup only, 5=fully unattended/self-healing |
| T8 | Portability | 2 | 0=single platform, 5=multi-platform with full docs/maintenance plan |
| T9 | Easy to change | 1 | 0–5 = number of: flexible reporting (simple/medium/complex), online-maintainable business data (next-day/immediate) |
| T10 | Concurrent use | 1 | 0=no concurrent access, 5=always concurrent + deadlock analysis + special tools |
| T11 | Special security | 1 | 0=no req, 5=detailed security plan + user support documented |
| T12 | 3rd party code access | 1 | 0=high-quality 3rd party code used widely, 5=no 3rd party or poor-quality code |
| T13 | User training | 1 | 0=no special req, 5=geographically dispersed users + detailed training plan |

**Rating scale**: 0 = not present/applicable, 3 = average, 5 = strongly present/essential

**Ricons example**: TFactor = 55 → TCF = 0.6 + 0.55 = **1.15**

---

## Step 4: EF — Environment Factor

Rate each environment factor E1–E8.

```
EFactor = Σ(Ei × Wi)
EF = 1.4 + (−0.03 × EFactor)
```

| Factor | Description | Weight |
|--------|-------------|--------|
| E1 | Familiar with development process used | 1.5 |
| E2 | Application experience | 0.5 |
| E3 | Object-oriented experience | 1 |
| E4 | Lead analyst capability | 0.5 |
| E5 | Motivation | 1 |
| E6 | Stable requirements | 2 |
| E7 | Part-time staff | −1 |
| E8 | Difficult programming language | −1 |

**Note**: E7 and E8 have negative weights — high scores on these reduce EFactor, which increases EF (less favorable environment).

**Ricons example**: EFactor = 13 → EF = 1.4 − 0.39 = **1.01**

---

## Step 5: UCP & Effort

```
UCP = UUCP × TCF × EF
    = 59 × 1.15 × 1.01
    ≈ 68.5
```

## Step 4b: EF Factor Descriptions

| Factor | Description | Weight | 0 → 5 scale |
|--------|-------------|--------|-------------|
| E1 | Familiar with dev process | 1.5 | 0=no experience, 5=more than half the team used it in multiple projects |
| E2 | Application domain experience | 0.5 | 0=no one has domain exp, 5=all have 2+ years in same domain |
| E3 | OO experience | 1 | 0=no OO experience, 5=all have 2+ years OO analysis/design/coding |
| E4 | Lead analyst experience | 0.5 | 0=none, 5=3+ years in multiple similar projects |
| E5 | Motivation | 1 | 0=completely unmotivated (needs constant supervision), 5=highly motivated (self-directed always) |
| E6 | Requirements stability | 2 | 0=historically very unstable/many changes, 5=completely stable historically |
| E7 | Part-time staff | −1 | 0=no part-timers, 5=>60% are part-time (negative weight — high value = bad) |
| E8 | Difficult programming language | −1 | 0=all very experienced programmers, 5=all inexperienced (negative weight) |

### PHM — Person-Hours per UCP

Count unfavorable environment factors:
- E1 < 3, E2 < 3, E3 < 3, E4 < 3, E5 < 3 → each one below threshold is "unfavorable"
- E6 < 3 → unfavorable
- E7 > 3, E8 > 3 → unfavorable

| Unfavorable count | PHM |
|------------------|-----|
| ≤ 2 | 20 |
| 3–4 | 28 |
| ≥ 5 | 36 (project at risk) |

**Effort = UCP × PHM**

**Ricons**: 4 unfavorable → PHM=28 → Effort = 68.5 × 28 ≈ **1,919 person-hours**

---

## Step 6: Timeline & Team Size

```
Monthly effort (person-months) = Effort / Hours_per_month
Optimal team size T = 2.5 × E^(1/3)   [McConnell 1996]
Duration = E / team_size
```

With 160h/month and 5 members:
- Monthly effort = 1919/160 = 12 person-months
- Optimal T = 2.5 × 12^(1/3) ≈ 5.8 people
- Duration = 12/5 ≈ 2.4 months theoretical → **3–4 months realistic** (coordination overhead)

---

## Quick Reference: Typical Values

### Typical small student projects (5 UCs, 5 members)
- UAW: 5–20 (mix of GUI users and API systems)
- UUCW: 25–75 (mostly medium UCs)
- UUCP: 30–90
- TCF: 0.85–1.25 (distributed apps → higher)
- EF: 0.65–1.15 (unfamiliar tech → higher EF = worse)
- UCP: 20–100
- PHM: 20 or 28 typically
- Effort: 400–2800 hours

### Common mistakes
1. Counting actor instances instead of actor types (e.g., counting each customer separately)
2. Counting all use cases including `<<include>>` sub-UCs (count only top-level business UCs)
3. Forgetting to count boundary system actors (payment gateway, map API) as Simple actors
4. Confusing PHM lookup — count *unfavorable* E-factors, not total E-factors
5. Using number of steps in ALL flows instead of just the main flow for UUCW classification

---

## Ricons Complete UCP Table

| | | Value |
|--|--|-------|
| **UAW** | 3×Simple(1) + 2×Complex(3) | **9** |
| **UUCW** | 1×Simple(5) + 3×Medium(10) + 1×Complex(15) | **50** |
| **UUCP** | 9 + 50 | **59** |
| **TFactor** | Sum T1–T13 | **55** |
| **TCF** | 0.6 + 0.01×55 | **1.15** |
| **EFactor** | Sum E1–E8 | **13** |
| **EF** | 1.4 − 0.03×13 | **1.01** |
| **UCP** | 59 × 1.15 × 1.01 | **≈68.53** |
| **Unfavorable E-factors** | 4 | → PHM = **28** |
| **Effort** | 68.53 × 28 | **≈1,919 hours** |
| **Timeline (5 people, 160h/mo)** | 1919 / (5×160) | **≈2.4 mo → 3–4 mo realistic** |
