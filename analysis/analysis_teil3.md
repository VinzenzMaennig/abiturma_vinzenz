---
marp: true
author: Vinzenz Maennig
math: mathjax
theme: gaia
class: 
size: 4:3
paginate: True
style: |
  section {
    font-size: 28px;
  }
backgroundColor: white

title: Analysis Teil 3
description: Third part of the analysis slides, advanced topics
---
# Analysis Teil 3
- Extremwertaufgaben
- Steckbriefaufgaben
- Funktionsscharen
- Diskriminantenaufgaben

---
<!--header: Analysis | Extremwertaufgaben-->
<!--footer: Abiturma Abivorbereitungskurs | Ostern 2023 München | Vinzenz Männig-->
### Extremwertaufgaben
##### Kaninchengehege

---
##### Rezept
1. Skizze anfertigen, falls nicht in der Aufgabenstellung vorhanden
2. Funktionsterm für die zu maximierende/minimierende Größe mit *einer* Variable aufstellen
3. Extrema bestimmen
4. Ergebnis im Kontext interpretieren

---
##### Weiteres Beispiel
Sei P(u|v) ein Punkt auf dem Graphen von $f(x) = -x^2+4x$ mit $0 \leq u\leq 3$. Der Ursprung O, der Punkt P und der Punkt N(u|0) begrenzen ein Dreieck. Welchen Flächeninhalt A kann dieses Dreieck maximal haben?

---

---
### Extremwertaufgaben: Rechenblock

| Schwierigkeit | Aufgaben |
| ----------- | ----------- |
| leicht | |
| mittel | |
| schwer | 77, 78 |

Für Schnelle und Unterforderte:
- Aufgabe 87 ff.
- Altabitur 2020 Analysis
- Altabitur 2021 Analysis

---
---
### Steckbriefaufgaben
1. Allgemeinen Funktionsterm der gesuchten Funktionsart aufstellen und Ableitungen bilden
2. Informationen aus dem Aufgabentext in Gleichungen übersetzen und damit
ein Gleichungssystem aufstellen
3. Gleichungssystem lösen

---
##### Beispiel
Bestimme den Term einer ganzrationalen Funktion 3. Grades, deren Graph Gf am Ursprung einen Extrempunkt und einen Wendepunkt in $W( 1 | 1 )$ hat.
1. $f(x) = ax^3 + bx^2 + cx + d$
&nbsp;
&nbsp;
&nbsp;

2. $G_f$ geht durch Ursprung
$G_f$ hat Extrempunkt am Ursprung
$G_f$ hat Wendepunkt in $W( 1 | 1 )$
$G_f$ geht durch Punkt $W( 1 | 1 )$

---
$G_f$ geht durch Ursprung $\implies f(0) = 0$
$G_f$ hat Extrempunkt am Ursprung $\implies f^\prime(0) = 0$
$G_f$ hat Wendepunkt in $W( 1 | 1 )$ $\implies f^{\prime \prime}(1) = 0$
$G_f$ geht durch Punkt $W( 1 | 1 )$ $\implies f(1) = 1$

3. 

---
##### Beispielhaft Informationen
- "enthält den Punkt $P(a|b)$": $f(a) = b$
- "hat bei $x = a$ eine einfache NST": $f(a) = 0$
- "hat bei $x = a$ eine doppelte NST": $f(a) = 0$ und $^\prime(a) = 0$
- "hat bei $P( a | b)$ einen Extrempunkt": $f(a) = b$ und $f^\prime(a) = 0$
- "hat an der Stelle $x = a$ die Steigung m": $f^\prime(a) = m$

---
### Steckbriefe: Rechenblock

| Schwierigkeit | Aufgaben |
| ----------- | ----------- |
| leicht | |
| mittel | |
| schwer | 79, 80, 81, 85 |

Für Schnelle und Unterforderte:
- Aufgabe 87 ff.
- Aufgabenblatt Analysis Besondere Aufgabentypen
- Altabitur 2020 Analysis
- Altabitur 2021 Analysis

---
---
### Funktionsscharen
Was ist eine Schar?

---
##### Extrempunkte einer Schar
$f_t (x) = x^2 + 2tx + 2x + 1, \quad t ≥ 0.$

---
##### Gemeinsame Schnittpunkte
$f_t (x) = x^2 + tx + 1 - t$

---
### Scharen: Rechenblock

| Schwierigkeit | Aufgaben |
| ----------- | ----------- |
| leicht | |
| mittel | |
| schwer | 82, 83, 84 |

Für Schnelle und Unterforderte:
- Aufgabe 87 ff.
- Aufgabenblatt Analysis Besondere Aufgabentypen
- Altabitur 2020 Analysis
- Altabitur 2021 Analysis

---

---
### Bestimme einen Parameter so, dass ein Problem keine/eine/zwei Lösungen hat
Gegeben sind die Funktion $f(x) = x^2+4$ und die Geradenschar $g_a(x) = ax$. Bestimme alle $a$ für die $f(x)$ und $g(x)$ keinen Schnittpunkt haben.
##### Skizze

---

##### Berechnung

---

##### Diskriminante
Die Wurzel in der Mitternachtsformel $x_{1,2}=\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$ heißt Diskriminante. Der Term $b^2 - 4ac$ unter der Wurzel entscheidet darüber, wie viele Lösungen die Gleichung hat.
- $b^2 - 4ac < 0 \implies$ keine Lösung 
- $b^2 - 4ac = 0 \implies$ eine Lösung 
- $b^2 - 4ac > 0 \implies$ zwei Lösungen

Es muss also eine Ungeichung, wie bei den Definitionsbereichen gelöst werden!

---
##### Rezept
1. Allgemein Lösungsgleichung aufstellen
2. Nach dem "Problemfall" in der Gleichung suchen (eingeschränkter Definitionsbereich)
3. Ungleichung je nach Lösung gewünscht oder unerwünscht aufstellen und Lösen (wie mit Definitionsbereichen)

---
### Lösungsmengen: Rechenblock
- Bestimme einen Bereich für $a$, sodass $f(x) = \frac{1}{x}-2$ und $g_a(x)=ax$ keinen Schnittpunkt haben
- Bestimme einen Bereich für $a$, sodass $f(x) = \sqrt{x-1}$ und $g_a(x)=ax$ mindestens einen Schnittpunkt haben

Für Schnelle und Unterforderte:
- Aufgabe 87 ff.
- Aufgabenblatt Analysis Besondere Aufgabentypen
- Altabitur 2020 Analysis
- Altabitur 2021 Analysis

---
---