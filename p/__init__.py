def describe(df,median=True):
    res = df.describe().T
    N = df.shape[0]
    for c in df.columns:
        unique = len(df[c].unique())
        res.loc[c,'unique'] = unique
        res.loc[c,'unique%'] = unique/N
        vc = df[c].value_counts(dropna=False)
        p = vc / N
        res.loc[c,'bits_of_info_nan'] = -(p*np.log2(p)).sum()
        vc = vc.drop(np.nan,errors='ignore')
        p = vc / N
        res.loc[c,'bits_of_info'] = -(p*np.log2(p)).sum()
        if median is True and df[c].dtype in [np.int64,np.float64]: 
            res.loc[c,'median']=df[c].median()
    res['indexlike'] = (res['unique']==1)   
    output_columns = ['bits_of_info', 'bits_of_info_nan', 'unique', 'unique%', 'indexlike']
    if median==True: 
        output_columns += ['median']
    output_columns += ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']
    res = res[output_columns].sort_values('bits_of_info')
    return res
    