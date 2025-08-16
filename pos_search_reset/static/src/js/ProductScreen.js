/** @odoo-module */

import { _t } from "@web/core/l10n/translation";
import { patch } from "@web/core/utils/patch";
import { PosStore } from "@point_of_sale/app/store/pos_store";

patch(PosStore.prototype, {
    async addProductToCurrentOrder(product, options = {}) {
        const searchInput = document.querySelector(
            ".input-container input[placeholder='Search products...']"
        );

        if (searchInput) {
            searchInput.value = "";
            searchInput.dispatchEvent(new Event("input", { bubbles: true }));
        }
        return super.addProductToCurrentOrder(...arguments);
   }
});
