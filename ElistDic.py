class Les:
    def __init__(self):
        self.elements = [
            {
                "symbol": "H",
                "name": "Hydrogen",
                "atomic_number": 1,
                "type": "non-metal",
                "discovery_year": 1766,
                "chlorine_reaction": "H₂ + Cl₂ → 2HCl"
            },
            {
                "symbol": "He",
                "name": "Helium",
                "atomic_number": 2,
                "type": "noble gas",
                "discovery_year": 1868,
                "chlorine_reaction": "He + Cl₂ → No reaction (Inert noble gas)"
            },
            {
                "symbol": "Li",
                "name": "Lithium",
                "atomic_number": 3,
                "type": "alkali metal",
                "discovery_year": 1817,
                "chlorine_reaction": "2Li + Cl₂ → 2LiCl"
            },
            {
                "symbol": "Be",
                "name": "Beryllium",
                "atomic_number": 4,
                "type": "alkaline earth metal",
                "discovery_year": 1798,
                "chlorine_reaction": "Be + Cl₂ → BeCl₂"
            },
            {
                "symbol": "B",
                "name": "Boron",
                "atomic_number": 5,
                "type": "metalloid",
                "discovery_year": 1808,
                "chlorine_reaction": "2B + 3Cl₂ → 2BCl₃"
            },
            {
                "symbol": "C",
                "name": "Carbon",
                "atomic_number": 6,
                "type": "non-metal",
                "discovery_year": "ancient",
                "chlorine_reaction": "C + 2Cl₂ → CCl₄"
            },
            {
                "symbol": "N",
                "name": "Nitrogen",
                "atomic_number": 7,
                "type": "non-metal",
                "discovery_year": 1772,
                "chlorine_reaction": "N₂ + 3Cl₂ → 2NCl₃"
            },
            {
                "symbol": "O",
                "name": "Oxygen",
                "atomic_number": 8,
                "type": "non-metal",
                "discovery_year": 1774,
                "chlorine_reaction": "O₂ + 2Cl₂ → 2Cl₂O"
            },
            {
                "symbol": "F",
                "name": "Fluorine",
                "atomic_number": 9,
                "type": "halogen",
                "discovery_year": 1886,
                "chlorine_reaction": "No direct reaction: F₂ + Cl₂ → No reaction"
            },
            {
                "symbol": "Ne",
                "name": "Neon",
                "atomic_number": 10,
                "type": "noble gas",
                "discovery_year": 1898,
                "chlorine_reaction": "Ne + Cl₂ → No reaction"
            }
        ]
        self.elements += [
            {
                "symbol": "Na",
                "name": "Sodium",
                "atomic_number": 11,
                "type": "alkali metal",
                "discovery_year": 1807,
                "chlorine_reaction": "2Na + Cl₂ → 2NaCl"
            },
            {
                "symbol": "Mg",
                "name": "Magnesium",
                "atomic_number": 12,
                "type": "alkaline earth metal",
                "discovery_year": 1755,
                "chlorine_reaction": "Mg + Cl₂ → MgCl₂"
            },
            {
                "symbol": "Al",
                "name": "Aluminum",
                "atomic_number": 13,
                "type": "post-transition metal",
                "discovery_year": 1825,
                "chlorine_reaction": "2Al + 3Cl₂ → 2AlCl₃"
            },
            {
                "symbol": "Si",
                "name": "Silicon",
                "atomic_number": 14,
                "type": "metalloid",
                "discovery_year": 1824,
                "chlorine_reaction": "Si + 2Cl₂ → SiCl₄"
            },
            {
                "symbol": "P",
                "name": "Phosphorus",
                "atomic_number": 15,
                "type": "non-metal",
                "discovery_year": 1669,
                "chlorine_reaction": "2P + 3Cl₂ → 2PCl₃ (or PCl₅)"
            },
            {
                "symbol": "S",
                "name": "Sulfur",
                "atomic_number": 16,
                "type": "non-metal",
                "discovery_year": "ancient",
                "chlorine_reaction": "S + Cl₂ → SCl₂ (or S₂Cl₂)"
            },
            {
                "symbol": "Cl",
                "name": "Chlorine",
                "atomic_number": 17,
                "type": "halogen",
                "discovery_year": 1774,
                "chlorine_reaction": "Cl₂ + Cl₂ → No reaction"
            },
            {
                "symbol": "Ar",
                "name": "Argon",
                "atomic_number": 18,
                "type": "noble gas",
                "discovery_year": 1894,
                "chlorine_reaction": "Ar + Cl₂ → No reaction"
            },
            {
                "symbol": "K",
                "name": "Potassium",
                "atomic_number": 19,
                "type": "alkali metal",
                "discovery_year": 1807,
                "chlorine_reaction": "2K + Cl₂ → 2KCl"
            },
            {
                "symbol": "Ca",
                "name": "Calcium",
                "atomic_number": 20,
                "type": "alkaline earth metal",
                "discovery_year": 1808,
                "chlorine_reaction": "Ca + Cl₂ → CaCl₂"
            }
        ]
        self.elements += [
            {
                "symbol": "Sc",
                "name": "Scandium",
                "atomic_number": 21,
                "type": "transition metal",
                "discovery_year": 1879,
                "chlorine_reaction": "Sc + Cl₂ → ScCl₃"
            },
            {
                "symbol": "Ti",
                "name": "Titanium",
                "atomic_number": 22,
                "type": "transition metal",
                "discovery_year": 1791,
                "chlorine_reaction": "Ti + 2Cl₂ → TiCl₄"
            },
            {
                "symbol": "V",
                "name": "Vanadium",
                "atomic_number": 23,
                "type": "transition metal",
                "discovery_year": 1801,
                "chlorine_reaction": "2V + 3Cl₂ → 2VCl₃"
            },
            {
                "symbol": "Cr",
                "name": "Chromium",
                "atomic_number": 24,
                "type": "transition metal",
                "discovery_year": 1797,
                "chlorine_reaction": "2Cr + 3Cl₂ → 2CrCl₃"
            },
            {
                "symbol": "Mn",
                "name": "Manganese",
                "atomic_number": 25,
                "type": "transition metal",
                "discovery_year": 1774,
                "chlorine_reaction": "Mn + Cl₂ → MnCl₂"
            },
            {
                "symbol": "Fe",
                "name": "Iron",
                "atomic_number": 26,
                "type": "transition metal",
                "discovery_year": "ancient",
                "chlorine_reaction": "2Fe + 3Cl₂ → 2FeCl₃"
            },
            {
                "symbol": "Co",
                "name": "Cobalt",
                "atomic_number": 27,
                "type": "transition metal",
                "discovery_year": 1735,
                "chlorine_reaction": "Co + Cl₂ → CoCl₂"
            },
            {
                "symbol": "Ni",
                "name": "Nickel",
                "atomic_number": 28,
                "type": "transition metal",
                "discovery_year": 1751,
                "chlorine_reaction": "Ni + Cl₂ → NiCl₂"
            },
            {
                "symbol": "Cu",
                "name": "Copper",
                "atomic_number": 29,
                "type": "transition metal",
                "discovery_year": "ancient",
                "chlorine_reaction": "Cu + Cl₂ → CuCl₂"
            },
            {
                "symbol": "Zn",
                "name": "Zinc",
                "atomic_number": 30,
                "type": "transition metal",
                "discovery_year": "before 1000 BCE",
                "chlorine_reaction": "Zn + Cl₂ → ZnCl₂"
            }
        ]
        self.elements += [
            {
                "symbol": "Ga",
                "name": "Gallium",
                "atomic_number": 31,
                "type": "post-transition metal",
                "discovery_year": 1875,
                "chlorine_reaction": "Ga + Cl₂ → GaCl₃"
            },
            {
                "symbol": "Ge",
                "name": "Germanium",
                "atomic_number": 32,
                "type": "metalloid",
                "discovery_year": 1886,
                "chlorine_reaction": "Ge + Cl₂ → GeCl₄"
            },
            {
                "symbol": "As",
                "name": "Arsenic",
                "atomic_number": 33,
                "type": "metalloid",
                "discovery_year": "ancient",
                "chlorine_reaction": "As + Cl₂ → AsCl₃"
            },
            {
                "symbol": "Se",
                "name": "Selenium",
                "atomic_number": 34,
                "type": "non-metal",
                "discovery_year": 1817,
                "chlorine_reaction": "Se + Cl₂ → SeCl₂"
            },
            {
                "symbol": "Br",
                "name": "Bromine",
                "atomic_number": 35,
                "type": "halogen",
                "discovery_year": 1826,
                "chlorine_reaction": "Br₂ + Cl₂ → No direct reaction"
            },
            {
                "symbol": "Kr",
                "name": "Krypton",
                "atomic_number": 36,
                "type": "noble gas",
                "discovery_year": 1898,
                "chlorine_reaction": "Kr + Cl₂ → KrCl₂ (very unstable)"
            },
            {
                "symbol": "Rb",
                "name": "Rubidium",
                "atomic_number": 37,
                "type": "alkali metal",
                "discovery_year": 1861,
                "chlorine_reaction": "2Rb + Cl₂ → 2RbCl"
            },
            {
                "symbol": "Sr",
                "name": "Strontium",
                "atomic_number": 38,
                "type": "alkaline earth metal",
                "discovery_year": 1790,
                "chlorine_reaction": "Sr + Cl₂ → SrCl₂"
            },
            {
                "symbol": "Y",
                "name": "Yttrium",
                "atomic_number": 39,
                "type": "transition metal",
                "discovery_year": 1794,
                "chlorine_reaction": "Y + Cl₂ → YCl₃"
            },
            {
                "symbol": "Zr",
                "name": "Zirconium",
                "atomic_number": 40,
                "type": "transition metal",
                "discovery_year": 1789,
                "chlorine_reaction": "Zr + 2Cl₂ → ZrCl₄"
            }
        ]
        self.elements += [
            {
                "symbol": "Nb",
                "name": "Niobium",
                "atomic_number": 41,
                "type": "transition metal",
                "discovery_year": 1801,
                "chlorine_reaction": "Nb + 2Cl₂ → NbCl₄"
            },
            {
                "symbol": "Mo",
                "name": "Molybdenum",
                "atomic_number": 42,
                "type": "transition metal",
                "discovery_year": 1781,
                "chlorine_reaction": "Mo + 2Cl₂ → MoCl₄"
            },
            {
                "symbol": "Tc",
                "name": "Technetium",
                "atomic_number": 43,
                "type": "transition metal",
                "discovery_year": 1937,
                "chlorine_reaction": "Tc + 2Cl₂ → TcCl₄"
            },
            {
                "symbol": "Ru",
                "name": "Ruthenium",
                "atomic_number": 44,
                "type": "transition metal",
                "discovery_year": 1844,
                "chlorine_reaction": "Ru + 2Cl₂ → RuCl₃"
            },
            {
                "symbol": "Rh",
                "name": "Rhodium",
                "atomic_number": 45,
                "type": "transition metal",
                "discovery_year": 1803,
                "chlorine_reaction": "Rh + Cl₂ → RhCl₃"
            },
            {
                "symbol": "Pd",
                "name": "Palladium",
                "atomic_number": 46,
                "type": "transition metal",
                "discovery_year": 1803,
                "chlorine_reaction": "Pd + Cl₂ → PdCl₂"
            },
            {
                "symbol": "Ag",
                "name": "Silver",
                "atomic_number": 47,
                "type": "transition metal",
                "discovery_year": "ancient",
                "chlorine_reaction": "2Ag + Cl₂ → 2AgCl"
            },
            {
                "symbol": "Cd",
                "name": "Cadmium",
                "atomic_number": 48,
                "type": "transition metal",
                "discovery_year": 1817,
                "chlorine_reaction": "Cd + Cl₂ → CdCl₂"
            },
            {
                "symbol": "In",
                "name": "Indium",
                "atomic_number": 49,
                "type": "post-transition metal",
                "discovery_year": 1863,
                "chlorine_reaction": "In + Cl₂ → InCl₃"
            },
            {
                "symbol": "Sn",
                "name": "Tin",
                "atomic_number": 50,
                "type": "post-transition metal",
                "discovery_year": "ancient",
                "chlorine_reaction": "Sn + Cl₂ → SnCl₂ (or SnCl₄)"
            }
        ]
        self.elements += [
            {
                "symbol": "Sb",
                "name": "Antimony",
                "atomic_number": 51,
                "type": "metalloid",
                "discovery_year": "ancient",
                "chlorine_reaction": "Sb + Cl₂ → SbCl₃"
            },
            {
                "symbol": "Te",
                "name": "Tellurium",
                "atomic_number": 52,
                "type": "metalloid",
                "discovery_year": 1782,
                "chlorine_reaction": "Te + Cl₂ → TeCl₄"
            },
            {
                "symbol": "I",
                "name": "Iodine",
                "atomic_number": 53,
                "type": "halogen",
                "discovery_year": 1811,
                "chlorine_reaction": "Cl₂ + I₂ → 2ICl"
            },
            {
                "symbol": "Xe",
                "name": "Xenon",
                "atomic_number": 54,
                "type": "noble gas",
                "discovery_year": 1898,
                "chlorine_reaction": "Xe + Cl₂ → XeCl₂ (unstable)"
            },
            {
                "symbol": "Cs",
                "name": "Cesium",
                "atomic_number": 55,
                "type": "alkali metal",
                "discovery_year": 1860,
                "chlorine_reaction": "2Cs + Cl₂ → 2CsCl"
            },
            {
                "symbol": "Ba",
                "name": "Barium",
                "atomic_number": 56,
                "type": "alkaline earth metal",
                "discovery_year": 1808,
                "chlorine_reaction": "Ba + Cl₂ → BaCl₂"
            },
            {
                "symbol": "La",
                "name": "Lanthanum",
                "atomic_number": 57,
                "type": "lanthanide",
                "discovery_year": 1839,
                "chlorine_reaction": "La + 3Cl₂ → LaCl₃"
            },
            {
                "symbol": "Ce",
                "name": "Cerium",
                "atomic_number": 58,
                "type": "lanthanide",
                "discovery_year": 1803,
                "chlorine_reaction": "Ce + 3Cl₂ → CeCl₃"
            },
            {
                "symbol": "Pr",
                "name": "Praseodymium",
                "atomic_number": 59,
                "type": "lanthanide",
                "discovery_year": 1885,
                "chlorine_reaction": "Pr + 3Cl₂ → PrCl₃"
            },
            {
                "symbol": "Nd",
                "name": "Neodymium",
                "atomic_number": 60,
                "type": "lanthanide",
                "discovery_year": 1885,
                "chlorine_reaction": "Nd + 3Cl₂ → NdCl₃"
            }
        ]
        self.elements += [
            {
                "symbol": "Pm",
                "name": "Promethium",
                "atomic_number": 61,
                "type": "lanthanide",
                "discovery_year": 1945,
                "chlorine_reaction": "Pm + 3Cl₂ → PmCl₃"
            },
            {
                "symbol": "Sm",
                "name": "Samarium",
                "atomic_number": 62,
                "type": "lanthanide",
                "discovery_year": 1879,
                "chlorine_reaction": "Sm + 3Cl₂ → SmCl₃"
            },
            {
                "symbol": "Eu",
                "name": "Europium",
                "atomic_number": 63,
                "type": "lanthanide",
                "discovery_year": 1901,
                "chlorine_reaction": "Eu + 3Cl₂ → EuCl₃"
            },
            {
                "symbol": "Gd",
                "name": "Gadolinium",
                "atomic_number": 64,
                "type": "lanthanide",
                "discovery_year": 1880,
                "chlorine_reaction": "Gd + 3Cl₂ → GdCl₃"
            },
            {
                "symbol": "Tb",
                "name": "Terbium",
                "atomic_number": 65,
                "type": "lanthanide",
                "discovery_year": 1843,
                "chlorine_reaction": "Tb + 3Cl₂ → TbCl₃"
            },
            {
                "symbol": "Dy",
                "name": "Dysprosium",
                "atomic_number": 66,
                "type": "lanthanide",
                "discovery_year": 1886,
                "chlorine_reaction": "Dy + 3Cl₂ → DyCl₃"
            },
            {
                "symbol": "Ho",
                "name": "Holmium",
                "atomic_number": 67,
                "type": "lanthanide",
                "discovery_year": 1878,
                "chlorine_reaction": "Ho + 3Cl₂ → HoCl₃"
            },
            {
                "symbol": "Er",
                "name": "Erbium",
                "atomic_number": 68,
                "type": "lanthanide",
                "discovery_year": 1842,
                "chlorine_reaction": "Er + 3Cl₂ → ErCl₃"
            },
            {
                "symbol": "Tm",
                "name": "Thulium",
                "atomic_number": 69,
                "type": "lanthanide",
                "discovery_year": 1879,
                "chlorine_reaction": "Tm + 3Cl₂ → TmCl₃"
            },
            {
                "symbol": "Yb",
                "name": "Ytterbium",
                "atomic_number": 70,
                "type": "lanthanide",
                "discovery_year": 1878,
                "chlorine_reaction": "Yb + 3Cl₂ → YbCl₃"
            }
        ]
        self.elements += [
            {
                "symbol": "Pm",
                "name": "Promethium",
                "atomic_number": 61,
                "type": "lanthanide",
                "discovery_year": 1945,
                "chlorine_reaction": "Pm + 3Cl₂ → PmCl₃"
            },
            {
                "symbol": "Sm",
                "name": "Samarium",
                "atomic_number": 62,
                "type": "lanthanide",
                "discovery_year": 1879,
                "chlorine_reaction": "Sm + 3Cl₂ → SmCl₃"
            },
            {
                "symbol": "Eu",
                "name": "Europium",
                "atomic_number": 63,
                "type": "lanthanide",
                "discovery_year": 1901,
                "chlorine_reaction": "Eu + 3Cl₂ → EuCl₃"
            },
            {
                "symbol": "Gd",
                "name": "Gadolinium",
                "atomic_number": 64,
                "type": "lanthanide",
                "discovery_year": 1880,
                "chlorine_reaction": "Gd + 3Cl₂ → GdCl₃"
            },
            {
                "symbol": "Tb",
                "name": "Terbium",
                "atomic_number": 65,
                "type": "lanthanide",
                "discovery_year": 1843,
                "chlorine_reaction": "Tb + 3Cl₂ → TbCl₃"
            },
            {
                "symbol": "Dy",
                "name": "Dysprosium",
                "atomic_number": 66,
                "type": "lanthanide",
                "discovery_year": 1886,
                "chlorine_reaction": "Dy + 3Cl₂ → DyCl₃"
            },
            {
                "symbol": "Ho",
                "name": "Holmium",
                "atomic_number": 67,
                "type": "lanthanide",
                "discovery_year": 1878,
                "chlorine_reaction": "Ho + 3Cl₂ → HoCl₃"
            },
            {
                "symbol": "Er",
                "name": "Erbium",
                "atomic_number": 68,
                "type": "lanthanide",
                "discovery_year": 1842,
                "chlorine_reaction": "Er + 3Cl₂ → ErCl₃"
            },
            {
                "symbol": "Tm",
                "name": "Thulium",
                "atomic_number": 69,
                "type": "lanthanide",
                "discovery_year": 1879,
                "chlorine_reaction": "Tm + 3Cl₂ → TmCl₃"
            },
            {
                "symbol": "Yb",
                "name": "Ytterbium",
                "atomic_number": 70,
                "type": "lanthanide",
                "discovery_year": 1878,
                "chlorine_reaction": "Yb + 3Cl₂ → YbCl₃"
            }
        ]

    def get_all(self):
        return self.elements

    def getsymbol(self, symbol):
        for element in self.elements:
            if element["symbol"].lower() == symbol.lower():
                return element
        return None

    def FilterType (self, type_name):
        return [e for e in self.elements if e["type"].lower() == type_name.lower()]

    def sbnos(self, query):
        query = query.lower()
        return [
            e for e in self.elements
            if query in e["name"].lower() or query == e["symbol"].lower()
        ]
