from typing import Dict

import pandera as pa
from pandera.engines import pandas_engine

from ma.utils.pandas import ColumnSchema as CS

timestamp_check = pa.Column(pandas_engine.DateTime({"dayfirst": True}))

# fmt: off
REGO_SCHEMA: Dict[str, CS] = dict( 
    index                       =CS(check=pa.Column(int)),
    accreditation_number        =CS(check=pa.Column(str)),
    station_name                =CS(check=pa.Column(str)),
    station_tic                 =CS(check=pa.Column(float)),
    scheme                      =CS(check=pa.Column(str)),
    country                     =CS(check=pa.Column(str)),
    technology_group            =CS(check=pa.Column(str)),
    generation_type             =CS(check=pa.Column(str, nullable=True)),
    output_period               =CS(check=pa.Column(str)),
    certificate_count           =CS(check=pa.Column(int)),
    certificate_start           =CS(check=pa.Column(str)),
    certificate_end             =CS(check=pa.Column(str)),
    mwh_per_certificate         =CS(check=pa.Column(float)),
    issue_date                  =CS(check=timestamp_check),
    certificate_status          =CS(check=pa.Column(str)),
    status_date                 =CS(check=timestamp_check),
    current_holder              =CS(check=pa.Column(str)),
    company_registration_number =CS(check=pa.Column(str, nullable=True)),
)
# fmt: on

SIMPLIFIED_TECH_CATEGORIES = {
    "Photovoltaic": "SOLAR",
    "Hydro": "HYDRO",
    "Wind": "WIND",
    "Biomass": "BIOMASS",
    "Biogas": "BIOMASS",
    "Landfill Gas": "BIOMASS",
    "On-shore Wind": "WIND",
    "Hydro 20MW DNC or less": "HYDRO",
    "Fuelled": "BIOMASS",
    "Off-shore Wind": "WIND",
    "Micro Hydro": "HYDRO",
    "Biomass 50kW DNC or less": "BIOMASS",
}
