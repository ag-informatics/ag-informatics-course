# Module 3, Lab 3

## BEFORE THE LAB

In this lab, we will use new software. To save time, please following sections below to install them before the lab.

### SQLite

If you are using MacOS, SQLite should have been installed by default. To verify installation, open terminal and type `sqlite3`. You should see the prompt showing the version number. To exit, type `.quit`.

For Windows users, go to [https://www.sqlite.org/download.html](https://www.sqlite.org/download.html), scroll down to "Precompiled Binaries for Windows" and download `sqlite-tools-win-x64-xxx.zip`. Extract the zip file and you will see `sqlite3.exe`, this is your sqlite command tool. You can either double-click or execute through terminal (PowerShell). To exit, type `.quit`.

For Linux users, you can install sqlite3 your OS package management. For example, if you are using Debian or Ubuntu family, run the following command

```
sudo apt install sqlite3
```

Then you can verify the installation by typing `sqlite3` in the terminal. YOu should see the prompt showing the sqlite version. To exit, type `.quit`.

<!-- ### DBeaver -->

### Create a folder for lab 3

You will to create a new folder call "lab3" in the same repository that you used in lab 2. Your repository should look like as below.

```
lab2            <-- previous lab submission
lab3            <-- new folder for this lab
README.md       <-- optional
```

## Farm Management Software

We are going to create a basic version of farm management software by the end of this class. Each lab in module 3-6 will introduce you to new concepts that you will need to build the software. In this lab (module 3), we will start with the fundamental element: data model. However, farm is complicated and diverse. Thus, we will limit the complexity of the farm that we are going to build software for in this lab. The lab 3 farm is inspired by the classic farm simulation game ["Harvest Moon: Back to the nature"](https://en.wikipedia.org/wiki/Harvest_Moon:_Back_to_Nature) (Released in 1999)

![Harvest Moon](https://upload.wikimedia.org/wikipedia/en/b/bf/Harvest_Moon_Back_to_Nature.jpg)

<!-- Basic element -->

In the game, you are given a farmland from your grandfather. The farm was not in a good condition. Your job is restore the farm operation. Since, you have to work on the entire farm alone, there will be too many things to remember. For example, which crops do you grow and how many of each? So, let's start with designing the crop tracking database. In the farm, you will divide the land into multiple plots. In each plot, we will record following information

- plot number
- length
- width
- planted date
- crop
- note

Each plot will have only 1 crop. But one crop can by planted in many plots. Therefore, in the plot table, `crop` attribute (or column) will be a **foreign key** pointing to another table. In our case, that another table is crop table which will have following columns

- crop name
- maturity date
- note

Therefore, our data model will have two tables. Now, it is time to create them.

1. We need to create a new database. Starting by activate sqlite engine (as installed in the [section above](#sqlite))
2. Type `.open [path-to-lab3]/crop_record.db`. You can optionally add `path-to-lab3` (e.g. `.open D:/class/Tam-ASM532-Labs/lab3/crop_record.db`). Otherwise, you can just ignore path (just type `.open crop_record.db`). It will create a new database file in your terminal current location. (or open the database file, if you created earlier).
3. Type `.tables`. You should see nothing as we have not created any tables.
4. Type

```
create table crops (                        <-- create a new table name "crops"
    crop_id integer primary key,            <-- the first column is "crop_id", data type is integer (whole number) and it is the primary key
    crop_name text not null,                <-- the second column is "crop_name", data type is text (or string) and it cannot be null
    maturity_date integer not null,         <-- the third column is "maturity_date", data type is integer and it cannot be null
    note text                               <-- the last column is "note", data type is text, it could be null
);
```

Now, if you type `.tables` you should see one table as a return value since we just created it. Each table must has primary key column. Imagine as you open an excel spreadsheet, you will see a running number on the left as a row number. Primary key acts as row number for the table in any databases. Other two columns have `not null` as a condition. This condition prevents inserting row with null (blank) into these columns. The database engine will reject inserting operations. See this [tutorial](https://www.sqlitetutorial.net/sqlite-create-table/) for more detail about creating new tables.

5. To see the data inside the table, type `select * from crops;`. You should see nothing in return as we just create a new table.
6. Type

```
insert into crops (crop_name, maturity_date)
values (carrot, 70);
```

The command above will insert a row to table `crops` with two column `crop_name` with value "carrot" and `maturity_date` with value 70. Note that, you don't need to add value to column `crop_id` as it is a primary key. So, this column is managed by the database engine. You don't need to specify value for `note` column as it is optional (it does not have `not null` constrain).

7. You can type `select * from crops;`. This time, you will see a row as return value.
8. Your task is to insert at least 4 more rows into crops table. You can choose any crops you want. You don't need to worry about researching for accurate maturity date. Any reasonable numbers will be accepted. At least 2 rows must have values in `note` column. Record your inserts command in `insert_crop.txt`.

<!-- ERD -->

<!-- Field -->
<!-- Animal -->

<!-- Python & SQLite -->
<!-- Create, insert, query with SQL verify with SQLite-->
<!-- SQLalchemy & SQLite -->

## How to Submit your Lab

```
lab3/
    crop_record.db          <-- The database for crops and plots table
    insert_crop.txt         <-- Commands that you used for inserting rows into crops table
```

## License

[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

<!-- This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa] -->

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png

[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

"Introduction to Agricultural Informatics Course" by [Ankita Raturi, Purdue University](https://github.com/ag-informatics/ag-informatics-course) is licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.](http://creativecommons.org/licenses/by-nc-sa/4.0/)
