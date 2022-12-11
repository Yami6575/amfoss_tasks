use scraper::{Html, Selector};
fn main() {
    let url = "https://crypto.com/price";
    let response = reqwest::blocking::get(url).expect("Could not load url.");
    let body = response.text().expect("No response body found.");
    let document = Html::parse_document(&body);
    let crypto_selector = scraper::Selector::parse("tr.css-1cxc880").unwrap();
    let crypto_name_selector = scraper::Selector::parse("span.chakra-text.css-1jjcb1a").unwrap();
    let crypto_price_selector = scraper::Selector::parse("div.css-b1ilzc").unwrap();
    let crypto_24_hchange_selector = scraper::Selector::parse("td.css-1b7j986 p").unwrap();
    let crypto_24_hvolume_selector = scraper::Selector::parse("td.css-1nh9lk8").unwrap();
    let crypto_marketcap_selector = scraper::Selector::parse("td.css-1nh9lk8+td").unwrap();
    let mut wtr = csv::Writer::from_path("scrapeData.csv").expect("Could not create file.");
    wtr.write_record(&["Crypto Name", "Price", "24H Change","24H Volume","Market Cap"]).unwrap();
    for element in document.select(&crypto_selector) {
        let crypto_name_element = element.select(&crypto_name_selector).next().expect("crypto name");
        let crypto_name = crypto_name_element.text().collect::<String>();
        let crypto_price_element = element.select(&crypto_price_selector).next().expect("Could not select crypto price");
        let crypto_price = crypto_price_element.text().collect::<String>();
        let crypto_24_hchange_element = element.select(&crypto_24_hchange_selector).next().expect("Could not select 24hchange");
        let crypto_24change = crypto_24_hchange_element.text().collect::<String>();
        let crypto_24_hvolume_element = element.select(&crypto_24_hvolume_selector).next().expect("Could not select 24hvolume");
        let crypto_24hvolume = crypto_24_hvolume_element.text().collect::<String>();
        let crypto_marketcap_element = element.select(&crypto_marketcap_selector).next().expect("Could not select marketcap");
        let crypto_marketcap = crypto_marketcap_element.text().collect::<String>();
        wtr.write_record([&crypto_name, &crypto_price, &crypto_24change, &crypto_24hvolume, &crypto_marketcap]).expect("Could not create selector.");
    }
    wtr.flush().expect("Could not close file");
    println!("Done");
} 
