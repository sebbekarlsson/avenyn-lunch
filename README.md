# avenyn-lunch
> Python library to get all lunch menus at avenyn


## Usage

    from avenyn_lunch.AvenySession import AvenySession

    
    session = AvenySession()

    restaurants = session.get_restaurants()


> `restaurants` will contain a list of objects looking like this:

    [
        {
            "name": "coop-konsum-avenyn",
            "image": "https://www.avenyn.se/wp-content/uploads/2015/09/coop_dagens_final.jpg",
            "weekly_menu": [
                [
                    "Coops restaurang Top Notch serverar dagens tre varma r\u00e4tter p\u00e5 buff\u00e9 med tillh\u00f6rande sallad:",
                    "Chili con carne",
                    "Chili sin carne",
                    "Fisk med salvia och lime",
                    "Veckans soppa: Kr\u00e4mig broccoli och pr\u00e4stost"
                ],
                [
                    "Coops restaurang Top Notch serverar dagens tre varma r\u00e4tter p\u00e5 buff\u00e9 med tillh\u00f6rande sallad:",
                    "\u00d6rtbakad fl\u00e4sk med pestos\u00e5s",
                    "Falafel (vegansk)",
                    "Fisk med getost och valn\u00f6tter",
                    "Veckans soppa: Kr\u00e4mig broccoli och pr\u00e4stost"
                ],
                [
                    "Coops restaurang Top Notch serverar dagens tre varma r\u00e4tter p\u00e5 buff\u00e9 med tillh\u00f6rande sallad:",
                    "Korv stroganoff",
                    "Vegetarisk korv stroganoff",
                    "Fisk med \u00e4ggs\u00e5s",
                    "Veckans soppa: Kr\u00e4mig broccoli och pr\u00e4stost"
                ],
                [
                    "Coops restaurang Top Notch serverar dagens tre varma r\u00e4tter p\u00e5 buff\u00e9 med tillh\u00f6rande sallad:",
                    "Kyckling med dragon och citron",
                    "Quorn med dragon och citron",
                    "Fisk med chorizosm\u00f6r",
                    "Veckans soppa: Kr\u00e4mig broccoli och pr\u00e4stost"
                ],
                [
                    "Coops restaurang Top Notch serverar dagens tre varma r\u00e4tter p\u00e5 buff\u00e9 med tillh\u00f6rande sallad:",
                    "Kalssisk kalops",
                    "Vegetariska biffar",
                    "Fisk med fetaost och spenat",
                    "Veckans soppa: Kr\u00e4mig broccoli och pr\u00e4stost"
                ]
            ]
        }

        ...
    ]

## Install
> To install, run:

    python setup.py install

> You can also run:

    pip install avenyn-lunch
