LOG ANALYSIS

This project helps to solve 3 queries to find the 3 most viewed articles, most
popular authors and the days in which more than 1% of requests led to errors.

In order to run this project you must first download and install VirtualBox and
Vagrant in your machines.

1. Launch the VM using command
    vagrant up

2. Log into the VM
    vagrant ssh

3. Change the directory to /Vagrant

4. Connect psql and load the data in the database using command
    psql -d news -f newsdata.sql

This database includes 3 tables
    Author
    Articles
    Log

Look around the table using /dt after you have connected to the database

3 views have been created as
  1. create view total_res as select date(time), count(*) from log group by date(time);
  2. create view err_res as select date(time), count(*) from log where status != '200 OK' group by date(time);
  3. create view err_rate as select total_res.date, (100.0*err_res.count*1.0/total_res.count) as percent from total_res, err_res where total_res.date=err_res.date order by total_res.date;



In order to run the python file run the command
    python itemlog.py
