import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-oca-l10n-germany",
    description="Meta package for oca-l10n-germany Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-l10n_de_country_states',
        'odoo12-addon-l10n_de_location_nuts',
        'odoo12-addon-l10n_de_steuernummer',
        'odoo12-addon-l10n_de_tax_statement',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
