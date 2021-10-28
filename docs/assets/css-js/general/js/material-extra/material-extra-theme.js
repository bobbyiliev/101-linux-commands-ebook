/*
 * Source: https://github.com/facelessuser/pymdown-extensions/blob/main/docs/src/js/material-extra-theme.js
 */

(() => {

    const preferToggle = function (e) {
        if (localStorage.getItem("data-md-prefers-color-scheme") === "true") {
            document.querySelector("body").setAttribute("data-md-color-scheme", (e.matches) ? "dracula" : "default")
        }
    }

    const setupTheme = function (body) {
        const preferSupported = window.matchMedia("(prefers-color-scheme)").media !== "not all"
        let scheme = localStorage.getItem("data-md-color-scheme")
        let prefers = localStorage.getItem("data-md-prefers-color-scheme")

        if (!scheme) {
            scheme = "dracula"
        }
        if (!prefers) {
            prefers = "false"
        }

        if (prefers === "true" && preferSupported) {
            scheme = (window.matchMedia("(prefers-color-scheme: dark)").matches) ? "dracula" : "default"
        } else {
            prefers = "false"
        }

        body.setAttribute("data-md-prefers-color-scheme", prefers)
        body.setAttribute("data-md-color-scheme", scheme)

        if (preferSupported) {
            const matchListener = window.matchMedia("(prefers-color-scheme: dark)")
            matchListener.addListener(preferToggle)
        }
    }

    const observer = new MutationObserver(mutations => {
        mutations.forEach(mutation => {
            if (mutation.type === "childList") {
                if (mutation.addedNodes.length) {
                    for (let i = 0; i < mutation.addedNodes.length; i++) {
                        const el = mutation.addedNodes[i]

                        if (el.nodeType === 1 && el.tagName.toLowerCase() === "body") {
                            setupTheme(el)
                            break
                        }
                    }
                }
            }
        })
    })

    observer.observe(document.querySelector("html"), { childList: true })
})()

window.toggleScheme = function () {
    const body = document.querySelector("body")
    const preferSupported = window.matchMedia("(prefers-color-scheme)").media !== "not all"
    let scheme = body.getAttribute("data-md-color-scheme")
    let prefer = body.getAttribute("data-md-prefers-color-scheme")

    if (preferSupported && scheme === "default" && prefer !== "true") {
        prefer = "true"
        scheme = (window.matchMedia("(prefers-color-scheme: dark)").matches) ? "dracula" : "default"
    } else if (preferSupported && prefer === "true") {
        prefer = "false"
        scheme = "dracula"
    } else if (scheme === "dracula") {
        prefer = "false"
        scheme = "default"
    } else {
        prefer = "false"
        scheme = "dracula"
    }
    localStorage.setItem("data-md-prefers-color-scheme", prefer)
    body.setAttribute("data-md-prefers-color-scheme", prefer)
    body.setAttribute("data-md-color-scheme", scheme)
}
