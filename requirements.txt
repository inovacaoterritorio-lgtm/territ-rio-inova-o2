# 🗺 Território Inovação — Mapa de Startups Curitiba / PR

Mapa interativo do ecossistema de startups de Curitiba com **1.486+ empresas** georreferenciadas.

## 🚀 Como usar

Acesse pelo GitHub Pages ou clone e abra o `index.html` localmente (via servidor HTTP — não funciona com `file://` devido ao fetch do JSON).

```bash
# Servidor local rápido com Python
python -m http.server 8080
# Acesse: http://localhost:8080
```

## 📁 Arquivos

| Arquivo | Descrição |
|---|---|
| `index.html` | Página do mapa (Leaflet + MarkerCluster) |
| `startups_data.json` | Dados das startups (lat/lng, CNPJ, área, endereço) |
| `dados_cnpjs.csv` | Lista de CNPJs de entrada para o crawler |
| `scripts/crawler_cnpj.py` | Crawler que enriquece os dados via BrasilAPI + Nominatim |
| `scripts/requirements.txt` | Dependências Python |
| `.github/workflows/atualizar_dados.yml` | GitHub Actions para atualização automática |

## ⚙️ Adicionar novas startups

1. Edite `dados_cnpjs.csv` e adicione novos CNPJs
2. O GitHub Actions detecta a alteração e roda o crawler automaticamente
3. O `startups_data.json` é atualizado e o mapa reflete os novos dados

Para rodar manualmente:
```bash
pip install -r scripts/requirements.txt
python scripts/crawler_cnpj.py
```

## 🌐 GitHub Pages

1. Vá em **Settings → Pages**
2. Source: `Deploy from a branch` → `main` → `/ (root)`
3. Salve e aguarde ~1 minuto

## 🛠 Tecnologias

- [Leaflet.js](https://leafletjs.com/) — mapa interativo
- [Leaflet.markercluster](https://github.com/Leaflet/Leaflet.markercluster) — agrupamento de pins
- [CartoDB Dark Matter](https://carto.com/basemaps/) — tiles do mapa escuro
- [BrasilAPI](https://brasilapi.com.br/) — dados públicos de CNPJ
- [Nominatim / OpenStreetMap](https://nominatim.org/) — geocodificação de endereços
