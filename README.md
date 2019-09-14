# Excel to database
This project is try to read excel data and save it to a database. When excel data is saved in database an status would be created to show what happend to each row of the excel file. this status encompasses three different values. added, updated and failed.
Futhermore, if the excel header differ from fields of the database table (model) a translation can be passed to the database writer.
Validating data and modifying fields is another property of this project. Using inheritance the absract methods of the DatabaseReader and DatabaseWriter can be implemented to implement model specific validations and modifications. 
