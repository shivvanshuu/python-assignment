# media_utils.py - reusable helper functions (user-defined module)


def seconds_to_hms(total_seconds):
    """Convert seconds to an HH:MM:SS string."""
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def filter_by_rating(items, min_rating=4.0):
    """Return the items whose rating is at least min_rating."""
    selected = []
    for item in items:
        if item.rating >= min_rating:
            selected.append(item)
    return selected


def summarize_by_type(items):
    """Return {TYPE: {'count', 'total_seconds', 'avg_rating'}} for the given items."""
    summary = {}
    for item in items:
        key = item.media_type.upper()
        if key not in summary:
            summary[key] = {"count": 0, "total_seconds": 0, "rating_sum": 0.0}
        summary[key]["count"] += 1
        summary[key]["total_seconds"] += item.duration_sec
        summary[key]["rating_sum"] += item.rating

    for key in summary:
        data = summary[key]
        data["avg_rating"] = round(data.pop("rating_sum") / data["count"], 2)
    return summary
