# Conversion automatique AutoCAD (DXF) → QGIS (GeoPackage)

> **🔒 The source code in this repository is encrypted.**
> The archive `dxf-to-qgis.zip` is protected with **WinZip AES-256** encryption.
> The password is shared privately with recruiters / reviewers on request.

## What it does

Pipeline convertissant des DXF (infrastructure + câblage) en un GeoPackage unique conforme au schéma cible.

- **Traitement géométrique** : fusion et alignement des deux DXF via un point de contrôle partagé ; nettoyage, déduplication et simplification géométrique.
- **Enrichissement et snapping** : rattachement des étiquettes texte (type de chambre, CPS, PCO, fibre) et snapping des câbles sur la canalisation et des BPE sur les chambres (priorité Chambre > BPE > PCO).
- **Export GeoPackage** : couches Chambre, Canalisation, PCO, SRO, BPE, Câble FO, Tranchée avec le bon CRS ; traitement par lot d'un dossier complet de projets SRO.

## Results

- **50+ projets** convertis automatiquement en données SIG exploitables.
- Réduction drastique du travail manuel de redessin.

## Stack

Python · ezdxf · geopandas · shapely · pandas · PyYAML · GDAL

## Decrypt & run

```bash
pip install pyzipper
python3 decrypt.py          # prompts for the password, extracts to ./src
# or without the helper (7-Zip / WinZip / unzip all support AES-256):
7z x dxf-to-qgis.zip -p
```

## Integrity

Every file inside the archive is listed with its SHA-256 in `MANIFEST.sha256`.
Verify **from the repository root** (the paths are relative to it):

```bash
sha256sum -c MANIFEST.sha256      # Linux / macOS / Git Bash
certutil -hashfile src\main.py SHA256   # Windows, per file
```

---
*Ali Nouna — alinouna@gmail.com — linkedin.com/in/AliNouna*
