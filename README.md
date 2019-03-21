# Thingspeak1
Provide functions to upload and retrive data to thingspeak server in effective way.
#python
To retrive data from thingspeak
  we have a funcion retrivedata() which take 3 arguments out of which 1 is optional.
  1st argument is Channel ID
  2nd argument is read api ker
  *3rd argument is total number of fields you want to retrive
      Example call:
        Let ChannelID is 12345, read api is 123abcdef123 have 3 data fields to retrive
          then retrivedata('12345','123abcdef123',3) which return the data in the form of list
          



To upload data to thingspeak
  we have a funcion putdata() which take atleast 3 arguments but able to take as many arguments you gave.
  1st argument is write api key
  2nd argument is total number of varioius fields
  rest are the data corresponding to each field
        Example call:
        Let write api is 123abcdef123, have 2 data fields and data is hello python
          then retrivedata('123abcdef123',2,'hello','python') which return only true and false
        Let write api is 123abcdef123, have 3 data fields and data is hello python user
          then retrivedata('123abcdef123',3,'hello','python','user') which return only true and false
