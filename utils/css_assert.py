def assert_css_property(locator, property_name, expected_value):
    actual_value = locator.evaluate(
        f"el => getComputedStyle(el).getPropertyValue('{property_name}')"
    ).strip()

    assert actual_value == expected_value, f"Expected {property_name} to be '{expected_value}', but got '{actual_value}'"
