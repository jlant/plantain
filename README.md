# Plantain

Plantain is a prototype web application built using [Flask](http://flask.pocoo.org/) that
builds science plans by combining national templates with user specific content.

![landingpage][landingpage]

### Features

* View various templated national plans that can be viewed including the USGS quality assurance plan and data management plan.
* Users fill out forms to add specific content to a national template plan of interest.
* Automatic merging of user specific content into the appropriate location within the national plan.

### Run prototype application

Navigate to the project directory and double click on `app.py`.

Or, navigate to the project directory and run from the command line:

```
$ python app.py
```

### Requirements
python>=3.6.1
click==6.7
Flask==0.12.2
Flask-Bcrypt==0.7.1
Flask-Cors==3.0.2
Flask-Login==0.4.1
Flask-WTF==0.14.2
Jinja2==2.9.6
peewee==3.7.1
Werkzeug==0.12.2
WTForms==2.2.1

### License

This software is licensed under [CC0 1.0][CC0 1.0] and is in the [public domain][public domain] because it contains materials that originally
came from the [U.S. Geological Survey (USGS)][U.S. Geological Survey (USGS)], an agency of the [United States Department of Interior][United States Department of Interior]. For more
information, see the [official USGS copyright policy][official USGS copyright policy].

[Creative Commons]
![Creative Commons logo][Creative Commons logo]


### Disclaimer
This software is preliminary or provisional and is subject to revision. It is being provided to meet the need for timely
best science. The software has not received final approval by the U.S. Geological Survey (USGS). No warranty, expressed
or implied, is made by the USGS or the U.S. Government as to the functionality of the software and related material nor
shall the fact of release constitute any such warranty. The software is provided on the condition that neither the USGS
nor the U.S. Government shall be held liable for any damages resulting from the authorized or unauthorized use of the
software.

The USGS provides no warranty, expressed or implied, as to the correctness of the furnished software or the suitability
for any purpose. The software has been tested, but as with any complex software, there could be undetected errors. Users
who find errors are requested to report them to the USGS.

References to non-USGS products, trade names, and (or) services are provided for information purposes only and do not
constitute endorsement or warranty, express or implied, by the USGS, U.S. Department of Interior, or U.S. Government, as
to their suitability, content, usefulness, functioning, completeness, or accuracy.

Although this program has been used by the USGS, no warranty, expressed or implied, is made by the USGS or the United
States Government as to the accuracy and functioning of the program and related program material nor shall the fact of
distribution constitute any such warranty, and no responsibility is assumed by the USGS in connection therewith.

This software is provided "AS IS."

### Author
Jeremiah Lant <jlant@usgs.gov>


[landingpage]: static/img/landingpage.png
[public domain]: https://en.wikipedia.org/wiki/Public_domain
[CC0 1.0]: http://creativecommons.org/publicdomain/zero/1.0/
[U.S. Geological Survey (USGS)]: https://www.usgs.gov/
[United States Department of Interior]: https://www.doi.gov/
[official USGS copyright policy]: http://www.usgs.gov/visual-id/credit_usgs.html#copyright/
[Creative Commons]: http://creativecommons.org/publicdomain/zero/1.0/
[Creative Commons logo]: http://i.creativecommons.org/p/zero/1.0/88x31.png
