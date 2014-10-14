from Selenium2Library import Selenium2Library


class Selenium2LibraryExt(Selenium2Library):

    def get_all_texts(self, locator):
        """Returns the text value of elements identified by `locator`.
        See `introduction` for details about locating elements.
        """
        return self._get_all_texts(locator)

    def _get_all_texts(self, locator):
        elements = self._element_find(locator, False, True)
        texts = []
        for element in elements:
            if element is not None:
                texts.append(element.text)
        return texts if texts else None
