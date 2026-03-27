# 🎯 Jogo de Tiro ao Alvo OpenGL

Jogo de tiro ao alvo desenvolvido em Python com OpenGL (PyOpenGL + GLUT). O jogador controla um personagem que mira e atira em alvos móveis, acumulando pontos conforme acerta.

---

## 🖥️ Demonstração

O jogo exibe uma cena 2D com fundo verde (campo), dois alvos móveis de tamanhos diferentes, um personagem com animação e arma, e um placar de pontuação em tempo real.

---

## 🎮 Como Jogar

| Tecla | Ação |
|---|---|
| `↑` (seta cima) | Move o personagem para cima |
| `↓` (seta baixo) | Move o personagem para baixo |
| `←` (seta esquerda) | Atira |
| Botão direito do mouse | Abre o menu de opções |

### Menu (botão direito)
- **Pausar** — pausa o movimento dos alvos e do tiro
- **Iniciar** — retoma o jogo
- **Desligar** — fecha o jogo

### Pontuação
- Acertar o **alvo grande** → **+1 ponto**
- Acertar o **alvo pequeno** → **+2 pontos**

---

## ⚙️ Requisitos

- Python 3.x
- PyOpenGL
- PyOpenGL_accelerate (opcional, para melhor desempenho)
- freeglut (biblioteca GLUT)

---

## 🚀 Instalação

**1. Clone o repositório:**
```bash
git clone https://github.com/LeoCarrer/shooting-range-opengl.git
cd shooting-range-opengl
```

**2. Instale as dependências Python:**
```bash
pip install PyOpenGL PyOpenGL_accelerate
```

**3. Instale o freeglut** (caso necessário):

- **Windows:** Baixe o freeglut e adicione as DLLs ao PATH ou à pasta do projeto.
- **Linux (Debian/Ubuntu):**
  ```bash
  sudo apt-get install freeglut3-dev
  ```
- **macOS:**
  ```bash
  brew install freeglut
  ```

**4. Execute o jogo:**
```bash
python Jogo.py
```

---

## 🏗️ Estrutura do Projeto

```
shooting-range-opengl/
│
├── Jogo.py        # Código principal do jogo
└── README.md      # Documentação
```

---

## 🛠️ Tecnologias Utilizadas

- **Python 3** — linguagem principal
- **PyOpenGL** — bindings OpenGL para Python
- **GLUT / freeglut** — gerenciamento de janela, teclado e timers
- **OpenGL 2D (gluOrtho2D)** — renderização em coordenadas ortográficas

---

## 📐 Detalhes Técnicos

- Renderização via `GL_QUADS` para todos os elementos gráficos
- Dois timers independentes: um para mover os alvos (`Timer`, 15ms) e outro para o tiro (`Timer2`, 3ms)
- Detecção de colisão por bounding box (AABB)
- Coordenadas lógicas fixas: **250 × 166.666** unidades (independente do tamanho da janela)
