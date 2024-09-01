import httpx

YANDEX_SPELLER_URL = "https://speller.yandex.net/services/spellservice.json/checkText"


async def check_text(text: str):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(YANDEX_SPELLER_URL, params={"text": text})
            response.raise_for_status()
            corrections = response.json()  # Отладочная информация
            if not corrections:
                return text, []

            corrected_text = corrections[0]["s"][0]
            return corrected_text

    except httpx.HTTPStatusError as e:
        raise Exception(
            f"HTTP error occurred: {e.response.status_code} - {e.response.text}"
        )
    except Exception as e:
        raise Exception(f"An error occurred: {str(e)}")
