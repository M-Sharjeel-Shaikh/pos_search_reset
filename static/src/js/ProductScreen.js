/** @odoo-module */

import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { patch } from "@web/core/utils/patch";

patch(ProductScreen.prototype, {
    async addProductToOrder(product) {
        const searchInput = document.querySelector(
            ".input-container input[placeholder='Search products...']"
        );

        if (searchInput) {
            searchInput.value = "";
            searchInput.dispatchEvent(new Event("input", { bubbles: true }));
        }

        return await super.addProductToOrder(product);
    },
});
