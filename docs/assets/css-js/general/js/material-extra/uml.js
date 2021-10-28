/* Notes (as of Mermaid 8.7.0):
 * - Gantt: width is always relative to the parent, if you have a small parent, the chart will be squashed.
 *   Can't help it.
 * - Journey: Suffers from the same issues that Gantt does.
 * - Pie: These charts have no default height or width. Good luck pinning them down to a reasonable size.
 * - Git: The render portion is agnostic to the size of the parent element. But padding of the SVG is relative
 *   to the parent element. You will never find a happy size.
 *
 * Source: https://github.com/facelessuser/pymdown-extensions/blob/main/docs/src/js/uml.js
 *
 */

/**
 * Targets special code or div blocks and converts them to UML.
 * @param {string} className is the name of the class to target.
 * @return {void}
 */
export default className => {

    // Custom element to encapsulate Mermaid content.
    class MermaidDiv extends HTMLElement {

        /**
        * Creates a special Mermaid div shadow DOM.
        * Works around issues of shared IDs.
        * @return {void}
        */
        constructor() {
            super()

            // Create the Shadow DOM and attach style
            const shadow = this.attachShadow({ mode: "open" })
            const style = document.createElement("style")
            style.textContent = `
      :host {
        display: block;
        line-height: initial;
        font-size: 16px;
      }
      div.mermaid {
        margin: 0;
        overflow: visible;
      }`
            shadow.appendChild(style)
        }
    }

    if (typeof customElements.get("mermaid-div") === "undefined") {
        customElements.define("mermaid-div", MermaidDiv)
    }

    const getFromCode = function (parent) {
        // Handles <pre><code> text extraction.
        let text = ""
        for (let j = 0; j < parent.childNodes.length; j++) {
            const subEl = parent.childNodes[j]
            if (subEl.tagName.toLowerCase() === "code") {
                for (let k = 0; k < subEl.childNodes.length; k++) {
                    const child = subEl.childNodes[k]
                    const whitespace = /^\s*$/
                    if (child.nodeName === "#text" && !(whitespace.test(child.nodeValue))) {
                        text = child.nodeValue
                        break
                    }
                }
            }
        }
        return text
    }

    // We use this to determine if we want the dark or light theme.
    // This is specific for our MkDocs Material environment.
    // You should load your configs based on your own environment's needs.
    const defaultConfig = {
        startOnLoad: false,
        theme: "default",
        flowchart: {
            htmlLabels: false
        },
        er: {
            useMaxWidth: false
        },
        sequence: {
            useMaxWidth: false,
            noteFontWeight: "14px",
            actorFontSize: "14px",
            messageFontSize: "16px"
        }
    }
    mermaid.mermaidAPI.globalReset()
    // Non Material themes should just use "default"
    let scheme = null
    try {
        scheme = document.querySelector("[data-md-color-scheme]").getAttribute("data-md-color-scheme")
    } catch (err) {
        scheme = "default"
    }
    const config = (typeof mermaidConfig === "undefined") ?
        defaultConfig :
        mermaidConfig[scheme] || (mermaidConfig.default || defaultConfig)
    mermaid.initialize(config)

    // Find all of our Mermaid sources and render them.
    const blocks = document.querySelectorAll(`pre.${className}, mermaid-div`)
    const surrogate = document.querySelector("html")
    for (let i = 0; i < blocks.length; i++) {
        const block = blocks[i]
        const parentEl = (block.tagName.toLowerCase() === "mermaid-div") ?
            block.shadowRoot.querySelector(`pre.${className}`) :
            block

        // Create a temporary element with the typeset and size we desire.
        // Insert it at the end of our parent to render the SVG.
        const temp = document.createElement("div")
        temp.style.visibility = "hidden"
        temp.style.display = "display"
        temp.style.padding = "0"
        temp.style.margin = "0"
        temp.style.lineHeight = "initial"
        temp.style.fontSize = "16px"
        surrogate.appendChild(temp)

        try {
            mermaid.mermaidAPI.render(
                `_mermaid_${i}`,
                getFromCode(parentEl),
                content => {
                    const el = document.createElement("div")
                    el.className = className
                    el.innerHTML = content

                    // Insert the render where we want it and remove the original text source.
                    // Mermaid will clean up the temporary element.
                    const shadow = document.createElement("mermaid-div")
                    shadow.shadowRoot.appendChild(el)
                    block.parentNode.insertBefore(shadow, block)
                    parentEl.style.display = "none"
                    shadow.shadowRoot.appendChild(parentEl)
                    if (parentEl !== block) {
                        block.parentNode.removeChild(block)
                    }
                },
                temp
            )
        } catch (err) { } // eslint-disable-line no-empty

        if (surrogate.contains(temp)) {
            surrogate.removeChild(temp)
        }
    }
}
