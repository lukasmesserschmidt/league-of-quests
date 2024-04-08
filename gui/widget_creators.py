import customtkinter as ctk

from .. import constants
from .entry_base import DigitEntry, ScaleDigitEntry


def general_sw(
    master,
    title: str,
    textvariable: ctk.StringVar,
    unit: str = False,
    text_color: str = constants.TEXT_COLOR,
    row: int = 0,
):
    title_label = ctk.CTkLabel(master, text=f"{title}:", text_color=text_color)
    entry = DigitEntry(master, textvariable=textvariable, width=60)

    if unit:
        unit_label = ctk.CTkLabel(master, text=unit, text_color=text_color)
        unit_label.grid(row=row, column=2, sticky="w")

    title_label.grid(row=row, column=0, sticky="e")
    entry.grid(row=row, column=1, padx=10, pady=3, sticky="ew")


def quest_sw(
    master,
    title: str,
    textvariables: dict,
    quest_duration_scale_var: ctk.StringVar,
    competion_duration_scale_var: ctk.StringVar = False,
    text_color: str = constants.TEXT_COLOR,
    row: int = 0,
):
    title_label = ctk.CTkLabel(master, text=f"{title}:", text_color=text_color)
    checkbox = ctk.CTkCheckBox(
        master, variable=textvariables["unlocked"], text="", width=0
    )
    quest_duration_entry = ScaleDigitEntry(
        master,
        scale_var=quest_duration_scale_var,
        textvariable=textvariables["questduration"],
        width=10,
    )

    if competion_duration_scale_var:
        completion_duration_entry = ScaleDigitEntry(
            master,
            scale_var=competion_duration_scale_var,
            textvariable=textvariables["completionduration"],
            width=10,
        )
        completion_duration_entry.grid(row=row, column=3, padx=5, pady=3, sticky="ew")

    title_label.grid(row=row, column=0, padx=10, sticky="e")
    checkbox.grid(row=row, column=1, sticky="e")
    quest_duration_entry.grid(row=row, column=2, padx=5, pady=3, sticky="ew")
