from dataclasses import dataclass


# Reference resolution for all pixel constants
REF_WIDTH = 3840
REF_HEIGHT = 2160


@dataclass
class HudElementBounds:
    """Pixel bounds for a square HUD element at 4K reference (3840x2160).

    min_* values correspond to GlobalScale=0, max_* to GlobalScale=1.
    """
    min_size: int
    max_size: int
    min_x: int
    min_y: int
    max_x: int
    max_y: int
    center_relative: bool = True


@dataclass
class BarElementBounds:
    """Pixel bounds for a rectangular bar element at 4K reference (3840x2160)."""
    min_x_size: int
    max_x_size: int
    min_y_size: int
    max_y_size: int
    min_x: int
    max_x: int
    min_y: int
    max_y: int
    center_relative: bool = True


# -- HUD element definitions at 4K reference --
# Format from notes: [min_size, max_size, min_x, min_y, max_x, max_y]

ABILITY_BOUNDS: dict[int, HudElementBounds] = {
    1: HudElementBounds(80, 120, 1615, 1459, 1985, 1895),  # Q
    2: HudElementBounds(80, 120, 1703, 1459, 2118, 1895),  # W
    3: HudElementBounds(80, 120, 1791, 1459, 2251, 1895),  # E
    4: HudElementBounds(80, 120, 1879, 1459, 2384, 1895),  # R
}

SUMMONER_SPELL_BOUNDS: dict[int, HudElementBounds] = {
    1: HudElementBounds(59, 90, 1979, 2008, 1986, 1895),  # D
    2: HudElementBounds(59, 90, 2045, 2008, 2088, 1895),  # F
}

RECALL_BOUNDS = HudElementBounds(53, 80, 2339, 2555, 2053, 1996)
TRINKET_BOUNDS = HudElementBounds(53, 80, 2339, 2555, 1987, 1898)

HEALTH_BOUNDS = BarElementBounds(
    min_x_size=548, max_x_size=828,
    min_y_size=23, max_y_size=35,
    min_x=1553, max_x=1364,
    min_y=2093, max_y=2058,
)

RESOURCE_BOUNDS = BarElementBounds(
    min_x_size=548, max_x_size=828,
    min_y_size=23, max_y_size=35,
    min_x=1553, max_x=1364,
    min_y=2096, max_y=2063,
)

# Minimap: base size range 400-800px at 4K, further scaled by MinimapScale
MINIMAP_BASE_MIN = 400
MINIMAP_BASE_MAX = 800


def _lerp(a: float, b: float, t: float) -> float:
    """Linear interpolation between a and b by factor t (0.0 to 1.0)."""
    return a + (b - a) * t


def compute_element_rect(
    element_bounds: HudElementBounds | BarElementBounds,
    global_scale: float,
    window_x: int,
    window_y: int,
    window_width: int,
    window_height: int,
    dpi_scale: float = 1.0,
    start_pct: float = 0.0,
    end_pct: float = 1.0,
) -> tuple[int, int, int, int]:
    """Compute absolute screen rect (x, y, width, height) for a HUD element.

    Scales from 4K reference to actual window size, applies GlobalScale
    interpolation, DPI correction, and center-relative offset.
    """
    global_scale = max(0.0, min(1.0, global_scale))

    # Resolution scale factor: how the actual window compares to 4K reference
    scale_x = window_width / REF_WIDTH
    scale_y = window_height / REF_HEIGHT

    if isinstance(element_bounds, BarElementBounds):
        # Bar elements have separate x/y sizes
        full_w = _lerp(element_bounds.min_x_size, element_bounds.max_x_size, global_scale)
        h = _lerp(element_bounds.min_y_size, element_bounds.max_y_size, global_scale)
        ref_x = _lerp(element_bounds.min_x, element_bounds.max_x, global_scale)
        ref_y = _lerp(element_bounds.min_y, element_bounds.max_y, global_scale)

        # Apply percentage span for partial bar overlay
        w = full_w * (end_pct - start_pct)
        ref_x = ref_x + full_w * start_pct
    else:
        # Square elements
        size = _lerp(element_bounds.min_size, element_bounds.max_size, global_scale)
        ref_x = _lerp(element_bounds.min_x, element_bounds.max_x, global_scale)
        ref_y = _lerp(element_bounds.min_y, element_bounds.max_y, global_scale)
        w = size
        h = size

    # Scale to actual window resolution
    w = w * scale_x
    h = h * scale_y
    x = ref_x * scale_x
    y = ref_y * scale_y

    if element_bounds.center_relative:
        # Position is relative to horizontal center of the 4K reference
        # Shift by the difference between actual center and 4K center
        ref_center = REF_WIDTH / 2
        actual_center = window_width / 2
        x = x - (ref_center * scale_x) + actual_center

    # Apply DPI correction: window coords are in physical pixels,
    # but Qt positions in logical pixels
    x = x / dpi_scale
    y = y / dpi_scale
    w = w / dpi_scale
    h = h / dpi_scale

    # Convert to absolute screen position
    abs_x = window_x / dpi_scale + x
    abs_y = window_y / dpi_scale + y

    return int(abs_x), int(abs_y), int(w), int(h)


def compute_minimap_rect(
    global_scale: float,
    minimap_scale: float,
    window_x: int,
    window_y: int,
    window_width: int,
    window_height: int,
    dpi_scale: float = 1.0,
    flip_minimap: bool = False,
) -> tuple[int, int, int, int]:
    """Compute absolute screen rect for the minimap.

    Minimap sits in a bottom corner, scaled by both GlobalScale and MinimapScale.
    """
    global_scale = max(0.0, min(1.0, global_scale))

    scale_factor = window_width / REF_WIDTH

    # Base minimap size interpolated by GlobalScale
    base_size = _lerp(MINIMAP_BASE_MIN, MINIMAP_BASE_MAX, global_scale)
    # Further scaled by the in-game MinimapScale setting
    size = base_size * minimap_scale * scale_factor

    # Position in bottom corner
    margin = 0
    if flip_minimap:
        # Bottom-left
        x = window_x + margin
    else:
        # Bottom-right
        x = window_x + window_width - size - margin

    y = window_y + window_height - size - margin

    # DPI correction
    x = x / dpi_scale
    y = y / dpi_scale
    size = size / dpi_scale

    return int(x), int(y), int(size), int(size)
