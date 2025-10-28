from pages.pricing_page import PricingPage

def test_pricing_page_header(page):
    pricing_page = PricingPage(page)

    pricing_page.goto("https://tester.codersguru.pl/")
    pricing_page.open_pricing_page()

    assert "/cennik" in page.url, "Pricing page failed to open"

    header = pricing_page.get_page_header()
    assert header == "Cennik", f"Expected header : 'Cennik', got : '{header}'"