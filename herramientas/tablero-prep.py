import pandas as pd, json
B=[18,20,25,30,35,40,45,50,55,60,65,70,75,80,85,200]
out={'bins':['18-19','20-24','25-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','65-69','70-74','75-79','80-84','85+'],'anios':[2009,2012,2015,2018,2021,2024],'e':{},'tipo':{},'nb':{}}
for y in out['anios']:
    df=pd.read_csv(f'datos_procesados/agg_{y}.csv',usecols=['EDOCVE','TIPOSEC','SEXO','EDAD','LN','SV','NV'])
    df=df[df.EDAD>=18]
    df['b']=pd.cut(df.EDAD,B,right=False,labels=False)
    df['N']=df.SV+df.NV
    # by estado, sexo (0 h,1 m, 2 nb), bin
    g=df.groupby(['EDOCVE','SEXO','b'])[['SV','N']].sum()
    e={}
    for (ed,sx,b),r in g.iterrows():
        e.setdefault(int(ed),{}).setdefault(int(sx),[[0,0] for _ in range(15)])[int(b)]=[int(r.SV),int(r.N)]
    # national = sum
    nat={}
    for ed,d in e.items():
        for sx,arr in d.items():
            a=nat.setdefault(sx,[[0,0] for _ in range(15)])
            for i,(s,n) in enumerate(arr): a[i][0]+=s; a[i][1]+=n
    e[0]=nat
    # keep h,m; nb separately (tiny)
    out['e'][y]={ed:{'h':d.get(0),'m':d.get(1)} for ed,d in e.items()}
    nb=df[df.SEXO==2][['SV','N']].sum(); out['nb'][y]=[int(nb.SV),int(nb.N)]
    t=df.groupby(['EDOCVE','TIPOSEC'])[['SV','N']].sum()
    tp={}
    for (ed,ts),r in t.iterrows(): tp.setdefault(int(ed),{})[ts]=[int(r.SV),int(r.N)]
    natt={}
    for ed,d in tp.items():
        for ts,v in d.items():
            a=natt.setdefault(ts,[0,0]); a[0]+=v[0]; a[1]+=v[1]
    tp[0]=natt; out['tipo'][y]=tp
    print(y, len(df))
s=json.dumps(out,separators=(',',':'))
open('datos.json','w').write(s); print(len(s))
