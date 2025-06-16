def get_css_property(locator, property_name):
    return locator.evaluate(
        f"el => getComputedStyle(el).getPropertyValue('{property_name}')"
    ).strip()

