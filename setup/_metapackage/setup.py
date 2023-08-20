import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-open-synergy-opnsynid-hr",
    description="Meta package for open-synergy-opnsynid-hr Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-ssi_hr',
        'odoo14-addon-ssi_hr_employee_experience_from_work_address',
        'odoo14-addon-ssi_hr_employee_project_experience',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
