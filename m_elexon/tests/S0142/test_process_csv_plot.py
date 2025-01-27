from pathlib import Path

import pandas as pd
from pytest import approx

import m_elexon.S0142.plot as plot
import m_elexon.S0142.process_csv as process_csv


def run_simple(group_bms: bool) -> pd.DataFrame:
    load = process_csv.process_directory(
        input_dir=Path(__file__).parent / "data",
        bsc_lead_party_id="GOLD",
        group_bms=group_bms,
    )
    return load


def test_aggregated() -> None:
    load = run_simple(group_bms=True)
    assert load["BM Unit Metered Volume"].sum() == approx(-6945.599)
    assert len(load["BM Unit Id"].unique()) == 1


def test_disaggregated() -> None:
    load = run_simple(group_bms=False)
    assert load["BM Unit Metered Volume"].sum() == approx(-6945.599)
    assert len(load["BM Unit Id"].unique()) == 14


def test_plot() -> None:
    load = run_simple(group_bms=True)
    plot.get_fig(load)
