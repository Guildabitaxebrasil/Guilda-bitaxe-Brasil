# Guilda bitaxeBrasil

> O guia mais completo em português para mineradores Bitcoin com **Bitaxe** — do iniciante ao overclock extremo.

[![Bitaxe](https://img.shields.io/badge/Bitaxe-Open%20Source%20Mining-%23f7931a)](https://bitaxe.org)
[![ESP-Miner](https://img.shields.io/badge/ESP--Miner-AxeOS-%23f7931a)](https://github.com/bitaxeorg/ESP-Miner)
[![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9C%93-blue)](https://github.com/bitaxeorg)

---

## 🎯 Propósito do Projeto

Este projeto reúne, em português, **todo o conhecimento necessário para minerar Bitcoin com um Bitaxe** — um minerador ASIC open-source do tamanho de uma xícara. O site foi criado pela comunidade **Guilda bitaxeBrasil** para ajudar mineradores brasileiros a:

- Escolher o modelo de Bitaxe ideal (Max, Ultra, Supra, Gamma, GT, Hex)
- Atualizar o firmware (ESP-Miner / AxeOS) com segurança
- Fazer **overclock** respeitando limites térmicos e de voltagem
- Configurar pools de mineração (pool tradicional e **loteria solo** via CKPool)
- Entender a API do AxeOS para dashboards e automações
- **Calcular a rentabilidade** em tempo real (pool e solo)

---

## 📄 Páginas do Site

| Página | Arquivo | Conteúdo |
|--------|---------|----------|
| **Home / Guilda bitaxeBrasil** | `index.html` | Visão geral: o que é Bitaxe, modelos, comparação, primeiros passos, firmware, overclock, pools, API, troubleshooting, FAQ, riscos e avisos, links úteis e sobre a guilda |
| **Guia Gamma 601** | `bitaxe-gamma-601-guia-completo.html` | Guia detalhado do Bitaxe Gamma 601 (BM1370): especificações, firmware, overclock passo a passo, tabelas, limites térmicos, destravamento OC e configuração recomendada |

---
## 🎬 Conteúdo para Vídeo (YouTube)

Arquivos de apoio para o canal da Guilda no YouTube — acompanham o conteúdo do site:

| Arquivo | Conteúdo |
|---------|----------|
| `descricao-youtube.md` | Descrição pronta para colar no YouTube Studio: 3 sugestões de título, descrição principal com os 6 modelos e todos os tópicos, capítulos/timestamps, tags/hashtags, versão curta para o feed e seção extra com o guia do Gamma 601 |
| `legenda-video-4min.srt` | Legenda sincronizada (SRT) do vídeo de 4 minutos: introdução, os 6 modelos, firmware (3 métodos), overclock seguro, pools (solo vs tradicional), rentabilidade, API do AxeOS e dicas rápidas |

---

## ✨ Funcionalidades

### 🧮 Calculadora de Rentabilidade (interativa)
Presente nas **duas páginas**, com:
- **Alternador de moeda** R$ / US$ (câmbio fixo de 1 US$ = R$ 5,50)
- **Presets rápidos**: por modelo (Max → Hex) na home; por nível de overclock (Stock → Extremo) no guia
- **6 campos editáveis**: hashrate (TH/s), potência (W), tarifa de energia, preço do BTC, taxa do pool e hashrate da rede (EH/s)
- **Painel Pool**: BTC/dia, valor minerado, custo de energia, lucro líquido por dia e por mês
- **Painel Loteria Solo (CKPool)**: chance de bloco por dia, tempo médio estimado, chance em 1 e 10 anos e prêmio do bloco (3,125 BTC)
- Cálculo em **tempo real** a cada digitação ou clique

### 🏠 Home (`index.html`)
- **O que é Bitaxe**: introdução ao projeto open-source (open source, mineração solo, consumo e SHA-256)
- **Modelos**: Max, Ultra, Supra, Gamma (⭐ destaque), GT (Turbo) e Hex — com chip, hashrate, consumo, eficiência e voltagem
- **Comparação completa** em tabela lado a lado
- **Primeiros Passos**: guia rápido de configuração do zero (modelo, fonte, Wi-Fi, firmware e pool)
- **Firmware**: OTA pela web, Web Flasher (USB) e bitaxetool (CLI)
- **Overclock seguro**: destravamento via `?oc`, limites térmicos e voltagem
- **Pools**: CKPool (solo), OCEAN, ViaBTC, F2Pool, Braiins, Parasite Pool + suporte a **Stratum V2**
- **API do AxeOS**: endpoints REST e WebSockets com exemplos `curl`
- **Troubleshooting** e **FAQ** (accordion interativo)
- **Riscos e Avisos**: disclaimers sobre overclock, estimativas e segurança elétrica
- **Sobre a Guilda**: apresentação da comunidade com links para Telegram e GitHub

### 📖 Guia Gamma 601 (`bitaxe-gamma-601-guia-completo.html`)
- **Especificações técnicas** detalhadas (ASIC BM1370, ESP32-S3, OLED, fan PWM)
- **Atualização de firmware** em 3 métodos (OTA, Web Flasher, bitaxetool)
- **Overclock**: preparação obrigatória (fonte Mean Well, pasta Kryonaut, heatsinks), teste de baseline 24h e fases de frequência/voltagem
- **Tabela de overclock** com 5 níveis (Stock → Extremo, até 1.8+ TH/s)
- **Limites térmicos** (45°C → 75°C+)
- **Configuração recomendada** para iniciar (600 MHz / 1150 mV → ~1.3 TH/s)
- **Troubleshooting** com causas e soluções
- **Navegação**: scroll-spy, reveal sutil ao rolar, botão voltar ao topo e link de volta à página principal

### 🎨 Visual profissional
Redesign aplicado nas **duas páginas**:
- **Sem animações**: títulos sólidos (sem gradiente animado), hovers discretos, sem efeitos de brilho ou flutuação
- **Emojis reduzidos**: apenas em avisos (⚠️) e dicas (💡) — removidos de títulos, botões e cards
- **Tema claro/escuro** na home, transições rápidas (0,2s) e tipografia consistente (Inter + JetBrains Mono)

---

## 🚀 Como Executar Localmente

Não requer instalação nem dependências — é HTML/CSS/JS puro:

```bash
# Clone o repositório
git clone https://github.com/Guildabitaxebrasil/Guilda-bitaxe-Brasil.git
cd Guilda-bitaxe-Brasil

# Abra a página principal (ou arraste o arquivo para o navegador)
start index.html          # Windows
open index.html           # macOS/Linux
```

Ou sirva com um servidor local simples:

```bash
python -m http.server 8000
# Acesse http://localhost:8000
```

---

## 🌐 Publicação (GitHub Pages)

O projeto já contém o arquivo `.nojekyll` (necessário para o GitHub Pages servir arquivos HTML com nomes contendo números corretamente).

1. No GitHub, vá em **Settings → Pages**
2. Em **Branch**, selecione `main` e a pasta `/ (root)`
3. Salve — o site fica disponível em `https://Guildabitaxebrasil.github.io/Guilda-bitaxe-Brasil/`

---

## 🗂️ Estrutura do Projeto

```
.
├── index.html                            # Página principal da Guilda
├── bitaxe-gamma-601-guia-completo.html   # Guia detalhado do Gamma 601
├── descricao-youtube.md                 # Descrição para o vídeo do YouTube (copiar e colar no Studio)
├── legenda-video-4min.srt               # Legenda do vídeo de 4 minutos (SRT)
├── .nojekyll                             # Habilita GitHub Pages com nomes de arquivo com números
└── README.md                             # Este arquivo
```

---

## 🛠️ Stack Tecnológica

- **HTML5** semântico
- **CSS3** — design system com variáveis customizadas (`:root`), tema claro/escuro (home), visual sóbrio e profissional, sem animações (apenas transições de hover), scrollbar customizada
- **JavaScript puro (Vanilla JS)** — sem frameworks ou bibliotecas externas:
  - Calculadora de rentabilidade (IIFE)
  - Scroll-spy no menu, reveal sutil ao rolar (IntersectionObserver) e botão voltar ao topo
  - Accordion de FAQ e menu mobile na home
- **Google Fonts**: Inter (texto) + JetBrains Mono (código/números)

---

## 🔑 Dados de Referência Incluídos

### Modelos de Bitaxe
| Modelo | ASIC | Hashrate | Consumo | Eficiência |
|--------|------|----------|---------|------------|
| Max | BM1397 (S17) | ~400 GH/s | ~15W | 30-35 J/TH |
| Ultra | BM1366 (S19 XP) | ~400-500 GH/s | ~12W | ~24 J/TH |
| Supra | BM1368 (S21) | ~625-775 GH/s | ~12W | ~17 J/TH |
| **Gamma** | **BM1370 (S21 Pro)** | **~1.0-1.2 TH/s** | **15-21W** | **~15 J/TH** |
| GT (Turbo) | 2x BM1370 | ~2.0-2.15 TH/s | 35-43W | ~18 J/TH |
| Hex | 6x BM1366 | ~3.0-3.3 TH/s | 65-90W | 27-30 J/TH |

### Overclock Gamma 601 (referência)
| Nível | Frequência | Voltagem | Hashrate | Consumo |
|-------|-----------|----------|----------|---------|
| 🌿 Stock | 400-525 MHz | 1050 mV | 1.0-1.2 TH/s | ~15W |
| ✅ Seguro | 600 MHz | 1150 mV | ~1.3 TH/s | ~20W |
| 👍 Bom | 700 MHz | 1200 mV | ~1.5 TH/s | ~25W |
| ⚡ Avançado | 800 MHz | 1250 mV | ~1.6-1.7 TH/s | ~30W |
| 🔥 Extremo* | 850-900 MHz | 1250-1300 mV | ~1.8+ TH/s | ~35W+ |

### Pools
| Pool | Tipo | URL |
|------|------|-----|
| CKPool | Solo (loteria) | `solo.ckpool.org:3333` |
| OCEAN | Descentralizado | `stratum-v1.ocean.xyz:4444` |
| ViaBTC | Tradicional | Regional (via site) |
| F2Pool | Tradicional | `btc.f2pool.com:3333` |
| Braiins | Tradicional | `stratum.brains.com:3333` |
| Parasite | Solo Cooperativo | `parasite.space` |

### API do AxeOS (destaques)
- `GET /api/system/info` — informações completas
- `GET /api/system/scoreboard` — top 20 shares mais difíceis
- `PUT /api/system/pools/{slot}` — configurar pool (SV1/SV2)
- `POST /api/system/restart` — reiniciar
- `WS /api/ws/live` — telemetria em tempo real

---

## 👤 Autor e Créditos

- **Autor**: Guilda bitaxeBrasil (`@Guildabitaxebrasil`)
- **Comunidade**: [bitaxeorg](https://github.com/bitaxeorg) • [Telegram Bitaxe](https://t.me/bitaxe)
- **Dashboard inspirador**: [Miner Miner (Shesh)](https://github.com/alexandersshen/bitaxe-miner-miner) por alexandersshen

> Feito para a comunidade — um share de cada vez ⚡

---

## ⚠️ Aviso

Os valores de rentabilidade são **estimativas educativas** — a dificuldade da rede, o preço do BTC e as tarifas de energia mudam constantemente. Overclock envolve riscos; respeite sempre os limites de voltagem (máx. 1250 mV para uso 24/7) e temperatura (< 65°C).
