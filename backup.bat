@echo off

echo =====================================
echo      RESPALDO MONGODB COMERCIOTECH
echo =====================================

docker exec mongodb_gestion_app mongodump ^
--username app_gestion ^
--password AppPassword2026 ^
--authenticationDatabase ComercioTech ^
--db ComercioTech ^
--out /backup

echo.
echo Backup realizado correctamente.
pause