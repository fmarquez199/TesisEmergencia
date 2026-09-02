cd ~/TPC-H/dbgen
sudo mysql <base-de-datos> < dss.ddl
./dbgen -s 100
sudo mysql -e "SET GLOBAL local_infile=1;"
for table in *.tbl; do
	sudo mysql --local-infile <base-de-datos> -e "LOAD DATA LOCAL INFILE $table INTO TABLE ${table%.tbl} FIELDS TERMINATED BY '|';"
done