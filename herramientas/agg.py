import sys, zipfile, io, pandas as pd
from concurrent.futures import ProcessPoolExecutor
year = sys.argv[1]; out = sys.argv[2]
z = zipfile.ZipFile(f"datos/DatosAbiertos_DECEyEC_ConteosCensales{year}.zip")
parts = []
for n in z.namelist():
    if not n.endswith('.csv'): continue
    with z.open(n) as f:
        df = pd.read_csv(io.TextIOWrapper(f, encoding='utf-8-sig', errors='replace'),
            usecols=['AELEC','EDOCVE','MPIOCVE','SECCION','TIPOSEC','SEXO','EDAD','LN','SV','NV','NS'], low_memory=False)
    df['EDAD'] = pd.to_numeric(df['EDAD'], errors='coerce')
    g = df.groupby(['AELEC','EDOCVE','MPIOCVE','TIPOSEC','SEXO','EDAD'], dropna=False)[['LN','SV','NV','NS']].sum().reset_index()
    parts.append(g)
    sec = df.groupby(['AELEC','EDOCVE','MPIOCVE','SECCION','TIPOSEC'])[['LN','SV','NV','NS']].sum().reset_index()
    parts_sec.append(sec) if False else None
    print(year, n, len(df), flush=True)
pd.concat(parts).to_csv(out, index=False)
