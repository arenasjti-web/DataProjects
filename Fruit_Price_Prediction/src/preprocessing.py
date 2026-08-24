import unicodedata # para quitar caracteres especiales

def formatColNames(df):
    df.columns = (
        df.columns
        .map(remove_accents)
        .str.lower()
        .str.replace(' ', '_')
        .str.replace(r'[^a-z0-9_]', '', regex=True)# quitar caracteres especiales
    )

def formatCategorical(df,categorical_columns):
    for c in categorical_columns:
        df[c] = df[c].str.lower().str.replace(' ', '_')



def remove_accents(text):
    return ''.join(
        c for c in unicodedata.normalize('NFD', text) # normaliza lo que termina separando caracteres como 'ó' en ['o','´']
        if unicodedata.category(c) != 'Mn'# elimina caracteres con categoría "Mark, Nonspacing" ( modificadores como el acento)
    )

