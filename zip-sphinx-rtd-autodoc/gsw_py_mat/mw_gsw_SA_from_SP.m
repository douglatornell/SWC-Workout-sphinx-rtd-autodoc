function [] = mw_gsw_SA_from_SP(filename, SP, p, lon, lat)
  startup()
  y = gsw_SA_from_SP(SP, p, lon, lat)
  dlmwrite(filename, y, ',')
