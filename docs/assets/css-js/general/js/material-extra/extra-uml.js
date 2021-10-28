/*
 * Source: https://github.com/facelessuser/pymdown-extensions/blob/main/docs/src/js/extra-uml.js
 */

import uml from "./uml"

(() => {
    const onReady = function (fn) {
        document.addEventListener("DOMContentLoaded", fn)
        document.addEventListener("DOMContentSwitch", fn)
    }

    const observer = new MutationObserver(mutations => {
        mutations.forEach(mutation => {
            if (mutation.type === "attributes") {
                let scheme = mutation.target.getAttribute("data-md-color-scheme")
                if (!scheme) {
                    scheme = "default"
                }
                localStorage.setItem("data-md-color-scheme", scheme)
                if (typeof mermaid !== "undefined") {
                    uml("mermaid")
                }
            }
        })
    })

    onReady(() => {
        observer.observe(document.querySelector("body"), { attributeFilter: ["data-md-color-scheme"] })

        if (typeof mermaid !== "undefined") {
            uml("mermaid")
        }
    })
})()
