import typing

DbusStr = typing.Literal["s"]
VariantStr = tuple[DbusStr, str]

DbusBool = typing.Literal["b"]
VariantBool = tuple[DbusBool, bool]

DbusByteArray = typing.Literal["ay"]
VariantByteArray = tuple[DbusByteArray, bytes]

DbusStrArray = typing.Literal["as"]
VariantStrArray = tuple[DbusStrArray, list[str]]

Options = typing.TypedDict(
    "Options",
    {"auth.no_user_interaction": VariantBool},
    total=False,
)
