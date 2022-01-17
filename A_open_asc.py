import numpy as np

def openAsc(filename):
  """
  Ouvre un fichier de MNT .asc et renvoie un dictionnaire correspondant à toutes les informations contenues dans le fichier

  Parameters
  ----------
  filename : str
    nom du ficher .asc à ouvrir
  Returns
  -------
  dict
    description du fichier.
    Clés du dictionnaire :
      ncols: nombre de colonnes, int
      nrows: nombre de lignes, int
      xllcorner: coordonnée X du coin inférieur gauche, float 
      yllcorner: coordonnée Y du coin inférieur gauche, float
      dx: taille d'une case en X
      dy: taille d'une case en Y
      data: données du fichier MNT, np.array
  """
  result = {}
  try:
    with open(filename, 'r') as file:
      lines = file.readlines()
  except IOError:
    raise IOError("Le fichier MNT n'a pas été correctement ouvert")
  
  for i in range(6):
    try:
      line = lines[i]
    except IndexError:
      raise IOError("Le fichier .asc est mal formé : moins de 6 lignes d'en-tête")

    key, value = line.split()
    if i <= 1 :
      result[key] = int(value)
    else:
      result[key] = float(value)

  dem_list = []
  for line in lines[6:]:
    dem_list.append(np.array(line.split(), dtype=float))

  result['data'] = np.array(dem_list)

  return result