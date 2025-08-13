# Combined Documentation for droip (from Sitemap)
<!-- Source .knowledge file: droip/.knowledge -->
<!-- Source Sitemap URL: https://droip.com/wp-sitemap-posts-docs-1.xml -->
<!-- CSS Selector: .documentation-content -->



---

<!-- Source URL: https://droip.com/docs/layers/ -->

---

Layers

Layers represent the individual elements that make up a web page, stacked on top of one another. This allows you to easily access and manage all the elements used to create the page.

By utilizing layers, you can customize every aspect of your page at any time, providing a streamlined and efficient way to work within the editor.

### **How to Use Layers**

To access the Layers in Droip:

1. Locate the `Layers`icon on the left sidebar.
2. Open the Layers tab to view the organization of sections and their corresponding elements on the current page.
3. In the Layers Panel, you can manage all the elements present on your canvas.

![Layers Panel in Droip](https://droip.com/wp-content/uploads/2023/02/layers-in-droip.webp)

Each element in the Layers Panel can be interacted with for more control over your page’s design:

* **Three-Dots Menu**: Click beside each element to expand or collapse sections, rename elements, or delete them.
* **Visibility Toggle**: An eye icon is displayed next to each element. Click on it to hide or display the element on the page.

### **Layers Panel Features**

* **Visibility Toggle**: Control the visibility of elements by enabling or disabling them with a simple click.
* **Reordering Layers**: Drag and drop elements to change their order in the stacking sequence.
* **Rename**: Click the three-dot menu and select the **Rename** option to modify an element’s name.
* **Delete**: To remove an element, click the three-dot menu and choose **Delete**.

This layered structure makes it easy to manage, customize, and organize the elements of your page efficiently within the editor.

---

<!-- Source URL: https://droip.com/docs/position/ -->

---

Position

In Droip, you have the flexibility to adjust the placement of elements using **Position**. This property is accessible in the Style Panel on the right-hand side.

Types of Position
-----------------

Click on the dropdown at the top of this section to select the Position Type. Below is the list of the 5 different values the Position property has to offer:

### Static

![Static Position](https://droip.com/wp-content/uploads/2023/09/Static.webp)

Elements are positioned based on the usual flow of the document. Other values have no effect. This is set as the default value for Position.

### Relative

![Relative Position](https://droip.com/wp-content/uploads/2023/09/Relative.webp)

Elements flow normally but can be offset using top, right, bottom, and left values. This means that other elements will behave as if it is taking their usual position even when its offset.

### Absolute

![Absolute Position](https://droip.com/wp-content/uploads/2023/09/Absolute.webp)

Elements are removed from the usual flow of the document and positioned relative to their closest ancestor if any or placed relative to the initial [containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Containing_block).

The final Position is based on the top, right, bottom, and left values.

### Fixed

![Fixed position](https://droip.com/wp-content/uploads/2023/09/Fixed.webp)

Fixed positioning removes an element from the normal document flow and positions it relative to the viewport, which means it remains fixed in its position even when the page is scrolled. This is true regardless of the ancestor elements’ properties like transform, perspective, filter, or will-change.

The element’s final position is determined solely by the values specified for top, right, bottom, and left, without considering the properties of their ancestor elements.

### Sticky

![Sticky Position](https://droip.com/wp-content/uploads/2023/09/Sticky.webp)

Elements are positioned based on the usual flow of the document and then offset relative to the nearest scrolling ancestor and containing block based on top, right, bottom, and left values. Other elements’ Position is not affected by this offset.

Adjust Position Using Offset Values
-----------------------------------

You can adjust an element’s position using the following offset values:

* **Top:** Click on the top edge of the box model and drag upwards to increase its value and downwards to decrease it. You can also directly enter the value in its input field.
* **Right:** Click on the right edge of the box model and drag to the right to increase its value and to the left to decrease it. You can also directly enter the value in its input field.
* **Bottom:** Click on the bottom edge of the box model and drag it downwards to increase its value and upwards to decrease it. You can also directly enter the value in its input field.
* **Left:** Click on the left edge of the box model and drag to the left to increase its value and to the right to decrease it. You can also directly enter the value in its input field.
* **Z Index:** Drag the slider range to set the Z Index or enter the value into its input field.

Float & Clear
-------------

![Float & Clear position](https://droip.com/wp-content/uploads/2023/09/Float-Clear.webp)

Click on the `Float & Clear` button to open its settings. From here you can set the value for Float and Clear.

### Float

Choose how elements should align within their container:

* **None**: Element follows its natural position.
* **Right**: Element floats to the right.
* **Left**: Element floats to the left.

### Clear

Set whether an element should be moved below floating elements that precede it. In other words, this defines what will happen to an element that’s next to a floating element. Also, this property applies to both floating and non-floating elements.

For this property, you can set any one of the following three:

* **Both:** Element is pushed below both left and right floating elements.
* **Left:** Element is pushed below left floating elements.
* **Right:** Element is pushed below right floating elements.

---

<!-- Source URL: https://droip.com/docs/page-audit/ -->

---

Page Audit

The **Audit** feature in Droip, represented by a **triangle exclamation** icon, is a powerful tool designed to automatically assess your website’s accessibility. It helps ensure your site adheres to key accessibility standards, improving usability and SEO.

![Page Audit in Droip](https://droip.com/wp-content/uploads/2023/02/Page-Audit.webp)

Audit Checks
------------

The Audit feature evaluates the following aspects:

### 1. Alt Text Missing

This check identifies **media elements (images, videos, etc.)** that lack **alternative text (alt text)**. When you hover over this feature, it highlights the affected media elements.

**Why it matters**:

* Alt text is crucial for visually impaired users, allowing screen readers to describe image content.
* It ensures accessibility compliance.
* Helps improve SEO by providing search engines with relevant content descriptions.

### 2. Link Missing

This check detects **link blocks** that do not have valid URLs assigned. Hovering over this feature will highlight the affected links.

**Why it matters**:

* Ensures smooth navigation for users.
* Prevents broken or incomplete links that could disrupt user experience.

### 3. Class Name Missing

This check counts how many elements are missing **class names**. Hovering over this feature will show the elements without class names.

**Why it matters**:

* Organizes your website elements efficiently.
* Simplifies styling and customization.
* Enhances maintainability and consistency across your project.

By using the **Audit** feature in Droip, you can proactively improve your website’s **accessibility, usability, and SEO**, making it more user-friendly for all visitors.

---

<!-- Source URL: https://droip.com/docs/lottie/ -->

---

Lottie

Lottie animations can be used to add interactivity, enhance visual appeal, and improve user engagement.

Uploading a Lottie File
-----------------------

To access free Lottie animations, you can explore various sources like LottieFiles, UI8, and Iconscout. These websites provide an extensive collection of both free and premium Lottie animations that you can download and integrate into your projects.

To upload a Lottie JSON File in Droip, follow these steps:

1. Enable `JSON FILES` from `Droip WP dashboard` > `Settings` > `General`.
2. Add the `Lottie` element from the Elements panel.
3. Upload the desired `Lottie JSON file` and use it in your page design.

Lottie Settings
---------------

![Add Lottie Animations in Droip](https://droip.com/wp-content/uploads/2023/03/Lottie-Settings.webp)

Lottie settings allow you to configure various options related to Lottie animation for optimal performance and file size.

* **Looping:** Choose whether the Lottie animation should loop continuously or play only once. Enabling “Looping” allows the animation to play repeatedly until the user leaves the page.
* **Play in Reverse:** Reverse the Lottie animation to create a “rewind” effect, where the animation plays backward.
* **Play**: Set if the Lottie animation will play on Auto, on Hover, or on Click.
* **Change Lottie Sequence:** Replace the Lottie animation with a new Lottie file or pre-existing files from the media library.
* **Set Duration:** Specify the duration of the Lottie animation in seconds. This option helps control the animation speed or synchronize it with other elements on the page.
* **Render in SVG:** Choose whether to render the Lottie animation as an SVG image. SVG (Scalable Vector Graphics) format maintains animation quality even when scaled.
* **Render in Canvas:** Choose whether to render the Lottie animation as a Canvas image. Canvas, an HTML5 element, allows for programmatically drawing graphics and animations.

---

<!-- Source URL: https://droip.com/docs/structure/ -->

---

Structure

From the `Style Panel` > `Structure`, you can adjust an element’s Structure. Not only that, but you can also adjust its Padding and Margin from here.

Display
-------

![Structure Panel in Droip](https://droip.com/wp-content/uploads/2023/03/Display.webp)

You can adjust the Padding & Margin values for your elements from here.

**Padding:** Padding is the space between an element’s content and its border.

To adjust this space, drag the borders of the blue square at the center in the Display section. Moving away from the box will increase the Padding while moving toward it will decrease the Padding. Note that this value can never be negative.

**💡 Tip:** Hover over the inside area of the element to reveal blue-colored padding handles. While pressing Shift, drag any of these inward for consistent padding on all sides.

**Margin:** Margin is the space between the element’s edge and the canvas’s edge.

To adjust this space, from the Display section, drag any of the red lines that frame the white square. Moving away from the box will increase the Margin while moving toward it will decrease the Margin.

This value can be both positive and negative.

**💡 Tip:** Hover over the outside area of the element for the red-colored margin handles to appear and while pressing Shift, drag any of these outward to ensure uniform margin space on all sides.

Structure
---------

![Change Element Structure in Droip](https://droip.com/wp-content/uploads/2023/03/Structure.webp)

Below the Padding and Margin toggles, you will find a dropdown from where you can change an element’s Structure. Clicking on this will bring up the following options:

* **Block (Take full Width):** The element takes the entire width of the parent element and generates line breaks before and after itself.
* **Inline (Wrap):** The element does not generate line breaks after itself and so usually, the next element will be on the same line if there’s space. Defining Height and Width properties will have no effect.
* **Inline Block (Have height/width):** This allows you to set the width and height of the element, respects top and bottom margins/padding, and does not generate line breaks after itself, so the element can sit beside other elements.
* **None (Wrap):** The element is completely removed.
* **Flex (One directional):** The element behaves like a block element and its contents are placed in a flex structure.
* **Grid (Multi-directional):** The element behaves like a block element and its contents are placed in a grid structure.

---

<!-- Source URL: https://droip.com/docs/list/ -->

---

List

The List element is used to showcase a list of items on your webpage in an organized way, enhancing the readability and user experience. Lists come in two primary types: Ordered Lists and Unordered Lists.

* **Ordered List**: An Ordered List presents its items in a sequential order, typically using numerical or alphabetical labels.
* **Unordered List**: An Unordered List displays its items as simple bullet points, providing an unordered collection of related items.

List Item
---------

Each item within a List, known as a List Item, can contain not only text but also various other elements like images, links, and more, allowing for rich and engaging content.

Adding a List
-------------

To add a List to your webpage, follow these simple steps:

1. Click on the **Elements** tab in the Topbar to open the Elements Panel on the left-hand side.
2. Locate the **List** element under the Basic section within the Elements Panel.
3. Drag and drop the List element onto your canvas.

List Inline Editor
------------------

![Droip list inline editor](https://droip.com/wp-content/uploads/2023/09/List-Inline-Editor.webp)

Upon adding the List element, you can configure your list from the inline editor. Use this editor to determine the type of list you want to display:

* Click on the first icon to create an Unordered List.
* Click on the second icon to create an Ordered List.

### List Options

![List options of Droip](https://droip.com/wp-content/uploads/2023/09/List-Options.webp)

To access more list options, click on the three-dot icon to bring up the **List Options** window.

**List Type:** Select whether you want to use ordered or unordered lists. Clicking on these tabs won’t set the type but only let you access its style options.

**List Style:** Change the style of the bullet points from here. For Unordered Lists, you can choose between dot or star-shaped bullet points. Similarly, for Ordered Lists, you can choose between lettered or numbered bullet points. Your List Type will be set accordingly.

You can even choose to not use bullet points for your list by clicking on the hyphen icon that’s under each type.

Adding Content to a List
------------------------

To add content to your List, you must first use List Items, as the List itself acts as a container for List Items. Here’s how you can add content to your List:

1. In the `Elements` Panel, find the `List Item` element and drag and drop it into your List.
2. Inside the List Item element, add your desired content elements such as Paragraphs, Images, Buttons, etc.

Repeat this process to populate your List with multiple List Items. For detailed information on List Items, please refer to our [List Item](https://droip.com/docs/list-item/) documentation.

---

<!-- Source URL: https://droip.com/docs/flex/ -->

---

Flex

The Flex Element in Droip allows you to create flexible and responsive layouts using CSS Flexbox, all through a visual interface.

What Is Flex?
-------------

The Flex Element is a layout container in Droip that uses the power of CSS Flexbox to arrange its direct children (child elements) in 1 dimension, either row or column.

![Flex element in Droip](https://droip.com/wp-content/uploads/2023/09/What-is-Flex_.webp)

It’s perfect for building horizontal menus, vertical stacks, split layouts, sidebars, and more.

Flex Container and Flex Items
-----------------------------

A **Flex Container** is the parent element and the direct children of that element become **Flex Items**.

![Flex Container & Flex Items](https://droip.com/wp-content/uploads/2023/10/Flex-Container-and-Flex-Items.webp)

How to Add a Flex
-----------------

![How to Add a Flex in Droip](https://droip.com/wp-content/uploads/2023/02/how-to-add-a-flex-element.webp)

To enable the Flex display for any element that contains other elements inside it:

1. From the right-side panel, go to the `Structure` section.
2. Select `Flex (one-directional)` from the drop-down menu.

Alternatively, you can add a **Flex** element to your page from the **Elements Panel** to start from scratch.

1. Open the `Insert` > `Elements` Panel from the left sidebar.
2. Drag the `Flex` element onto your canvas.

Place your desired elements inside the Flex container (these will be Flex Items).

Flexbox Direction
-----------------

![Flexbox Direction in Droip](https://droip.com/wp-content/uploads/2023/02/flex-direction.webp)

The flex-direction property determines the direction in which the flex items are laid out.

* Row (Default): Items are laid out horizontally, from left to right.
* Row Reverse: Items are laid out horizontally, from right to left.
* Column: Items are laid out vertically, from top to bottom.
* Column Reverse: Items are laid out vertically, from bottom to top.

**Use Case**: Choose row for horizontal navigation bars and column for stacked content like cards or list items.

Cross-Axis
----------

The `cross-axis` is the perpendicular axis to the main axis within a flex container. The main axis is defined by the flex-direction property, which can be set to a row or column.

For example, if the flex-direction is set to row, then the main axis will be horizontal, and the cross-axis will be vertical.

Flex Wrapping
-------------

The `flex-wrap` property sets whether flex items are forced onto one line or can wrap onto multiple lines. By default, Flex items stay on a single line.

**Nowrap**

![Nowrap Property in Flex](https://droip.com/wp-content/uploads/2023/02/no-wrap.webp)

The flex items are laid out in a single line, which may cause the flex container to overflow.

**Wrap**

![Wrap Property in Flex](https://droip.com/wp-content/uploads/2023/02/wrap.webp)

Items wrap onto multiple lines from top to bottom (or left to right).

**Wrap-reverse**

![Wrap-reverse Property in Flex](https://droip.com/wp-content/uploads/2023/02/wrap-reverese.webp)

Behaves the same as wrap, but in reverse order.

Flex Gap
--------

![Flex Gap Property in Droip](https://droip.com/wp-content/uploads/2023/02/flex-gap.webp)

The Gap setting lets you control the spacing between flex items, both row gap and column gap.

* Row Gap – space between items in the same row.
* Column Gap – space between items in different columns.

With Flex Gap, you can easily create consistent spacing between cards, icons, or buttons without adding padding/margin manually.

Align Content
-------------

![Align Content in Droip](https://droip.com/wp-content/uploads/2023/02/align-items.webp)

Controls the alignment of items along the cross axis (perpendicular to the main axis).

* Flex Start: Align items to the start of the cross-axis
* Center: Center items along the cross-axis
* Flex End: Align items to the end of the cross-axis
* Baseline: Align items based on their text baseline

### Alignment for Multi-line flex

![Alignment for Multi-line flex ](https://droip.com/wp-content/uploads/2023/02/align-multi-line-flex.webp)

When there are multiple lines of flex items (e.g., wrapping is enabled), you get additional alignment options. It controls the space between rows on the cross-axis.

* Flex Start / End: Align lines to start, or end of cross-axis
* Space Between / Around / Evenly: Apply spacing between multiple rows
* Stretch: Rows stretch to fill the container

Justify Content
---------------

![Justify Content in Droip](https://droip.com/wp-content/uploads/2023/02/justify-content.webp)

The `justify` property controls the alignment of items along the main axis (the direction defined by flex-direction).

* `Flex-start`: Items are aligned to the left (start) of the container.
* `Flex-end`: Items are aligned to the right (end) of the container.
* `Center`: Items are centered horizontally within the container.
* `Space-between`: Items are evenly distributed in the container, with space between each item.
* `Space-around`: Items are evenly distributed in the container, with space around them.

**Use Case**: Use space-between for equal distribution (e.g., navigation links), or center for symmetrical designs.

**📝 **Note****: Many of these options can also be found on the Flex Controller. To access this controller, simply click on the blue settings icon on the flex element’s top-right corner.

Flex Child
----------

A flex child is also referred to as a flex item. In Droip, each child inside the Flex container also have its own flex-specific settings for more granular control.

![Individual Flex Item Controls in Droip
](https://droip.com/wp-content/uploads/2023/02/individual-flex-item-controls.webp)

### Self Align

The `align-self` property controls the alignment of individual flex items along the cross-axis of the flex container. It applies only to individual flex items, whereas `align-items` applies to all flex items within the container.

**Available Values for align-self**:

* `flex-start`: Aligns the item to the start (top) of the cross-axis.
* `center`: Centers the item along the cross-axis.
* `flex-end`: Aligns the item to the end (bottom) of the cross-axis.
* `stretch`: Stretches the item to fill the entire cross-axis of the container.
* `baseline`: Aligns the item’s baseline with the baseline of other flex items in the container. This option is typically used for aligning text within a line of text.

### Order

The `Order` property controls the order in which flex items appear within the flex container.

By default, all flex items have an order value of 0, but you can change it to reorder items based on different screen sizes, create a responsive layout, or for accessibility reasons.

The order property accepts integer values, and you can assign a different order value to each flex item within the container. Flex items with lower order values appear first, followed by items with higher order values.

For example, if you set the order value of one flex item to -1 and another to 1, the flex item with the order value of -1 will appear first, followed by the flex item with an order value of 0, and then the flex item with an order value of 1.

### Flex Ratio

In Flex Ratio, you can set the `flex-basis`, `flex-grow`, and `flex-shrink` properties to create flexible and responsive layouts.

**`flex-basis`**

This property sets the initial size of a flex item along the main axis of the flex container. It specifies the default size of the flex item before any remaining space is distributed according to the `flex-grow` and `flex-shrink` properties.

The `flex-basis` property can be set to a length value, such as pixels or percentages, or it can be set to the auto keyword, which means the initial size of the item will be based on its content.

**`flex-grow`**

This property determines how much a flex item will grow when there is extra space available along the main axis. It accepts a unitless value that represents the proportion of available space that the flex item should take up relative to other flex items within the same flex container.

**`flex-shrink`**

This property controls how much a flex item will shrink when there is not enough space to accommodate all the items within the flex container. It also accepts a unitless value that represents the proportion of space that should be taken away from the item when

---

<!-- Source URL: https://droip.com/docs/pre-built-library/ -->

---

Pre-built Library

Apart from the usual elements in the Elements Panel, Droip also has a Pre-Built Library with a collection of more advanced pre-defined **Elements** and **Sections**.

To access them, head over to the **Pre-built Library** which you can access from the Elements tab on the **Topbar**.

Elements
--------

Below is a list of all of the Pre-Built Elements that you can use and the options available for each category.

### Buttons

As you know, buttons play a significant role on a webpage such as letting users submit a form, functioning as CTAs for users to take that last step, helping users maneuver the website, and more.

For that reason, sometimes you may need a bit more functionality from a button that a basic one can’t provide. So, here are a few advanced alternatives for the Button Element. Options include:

* **Button Fill:** Button filled with a solid background.
* **Button Outline:** Button with only an outline and no background fill.
* **Button Split:** Button split into an action button and a dropdown toggle.
* **Button Icon:** Button with no text and only an icon.
* **Button With Icon:** Button with text and icon.
* **Button Action:** Button with text and icon but no background fill or outline.
* **Button Link:** Button with only link text.

### Checkbox

Use Checkboxes to take multiple inputs from a list of options. Do note that you must add this element inside a Form element for it to appear.

### Radio

Use Radio buttons to take single input from a list of options. Do note that you must add this element inside a Form element for it to appear.

### Ratings

Ratings are a way for users to rank a product or service based on their experience to provide information for others to see. Incorporating a Rating and Review system is a great idea if you need to boost credibility.

Listed below are the variations of the Rating element offered that you can choose from!

* **Rating Stars**
* **Rating Half-Stars**
* **Rating Octagones**
* **Rating Half-Octagones**
* **Rating Emoji**

### Search Boxes

Search is another must-have element that you may need to include as helps users easily find what they’re looking for. Here we have 3 different styles of Search options:

* **Search Box:** Simple Search Box.
* **Search with Button:** Search Box with an icon button.
* **Search Underlined:** Search Box in an outline style.

### Steppers

A Stepper is a nifty input control that can be used to input numbers. This control consists of two parts – one button to increment and one to decrement the value along with its preview. Below is a list of the Stepper styles available:

* **Stepper Basic:** Value is displayed on the left and increment and decrement buttons are stacked up on the right.
* **Stepper Horizontal:** Buttons on either side with the value displayed in the middle.
* **Stepper Vertical:** Buttons on the top and bottom with the value displayed in the middle.

### Text Fields

Text Fields are a classic input control that you’ll need for any form. Here you’ll find a few more advanced versions of the element to further enhance your webpage.

* **Text Field Basic:** A basic Text Field you can use in any form for data input.
* **Text Field with Adjusting Height:** With this Text Field, if there is more content than there is space for, automatically more space will be added vertically but with a scroll so the real height of the element remains unchanged.

### Detail List

The Detail List Element is basically a pre-made data table and is the perfect choice for displaying a lot of information in a neat and simple way. Styles available are the following:

* **Detail List One:** Simple and neat styled table.
* **Detail List Two:** Table with grid lines.
* **Detail List Three:** Table with alternating colored rows.

### Tab

The Tab Pre-Built Element offers you a few more variations on your usual Tab element like the following:

* **Tab One:** Tab with Tab Menu on top of the Tab Pane.
* **Tab Two:** Tab with Tab Menu on the bottom of the Tab Pane.
* **Tab Three:** Tab with Tab Menu on the left of the Tab Pane.
* **Tab Four:** Tab with Tab Menu on the right of the Tab Pane.

### Teaching Bubble

A Teaching Bubble is a kind of tooltip element that consists of a button and a speech bubble. Within that speech bubble is a heading, text description, and a pair of Yes and No buttons.

Clicking on the button should make the bubble appear and clicking on the Yes/No buttons should make the bubble disappear.

Options include:

* **Teaching Bubble Left:** Teaching Bubble with a button on the left and bubble on the right.
* **Teaching Bubble Top:** Teaching Bubble with button at the top and bubble below.

### Callout

Callouts are similar to Teaching Bubbles but the Yes and No buttons are instead replaced with a Link. Clicking on the button will make the bubble appear and clicking on it again should make it disappear.

### Dialog

A Dialogue box is a pop-up like element with a message and two CTA options.

### Modals

You can create custom Pop-ups using our Pop-up Builder but also use the following templates to speed up the design process. Options include:

* Modal With X Button
* Modal Sign In
* Modal Newsletter
* Modal Success Message

### Tooltips

Tooltips are helpful messages for users that should appear on Hover. For this, we have the following variations:

* Tooltip Top
* Tooltip Bottom
* Tooltip Left
* Tooltip Right

### Alerts

Alerts are warning message templates and available are the following types:

* **Alert:** Simple Alert message.
* **Alert with CTA:** Alert message with Call to Action Buttons.

### Avatar Group

An Avatar Group is basically a grouping of User Avatars and you can choose between the following styles:

* **Avatar Group Circle:** Avatar Group with circular images.
* **Avatar Group Square:** Avatar Group with square images.

### Cards

Cards are a great way to display a group of related content on a page. You can use these on a feature list page, a product archive page, and more.

* **Card Basic:** Basic Card with a heading and a description text.
* **Card Button:** Card with a heading, description, and a call to action button.
* **Card Icon:** Card with a heading, description, icon, and a call to action button.
* **Card Image Button:** Card with a heading, description, image, and a call to action button.

### Notifications

Notifications are small dialog boxes that can be used to notify users about something.

* **Notification Inline:** Consists of a heading and a button all arranged inline.
* **Notification Text:** Consists of a heading and some text with an x icon on the top-right.

Sections
--------

![Sections of Droip](https://droip.com/wp-content/uploads/2023/09/Sections.webp)

Next up we have `Pre-Built Sections` which you can access by clicking on its icon on the from the Pre-built Library.

Here, you’ll find a plethora of ready-made sections that you can use to speed up your design process and you can also fully customize them to match your preferences using the settings in the `Style Panel`.

---

<!-- Source URL: https://droip.com/docs/media-manager/ -->

---

Media Manager

![](https://droip.com/wp-content/uploads/2023/03/Accessing-media.webp)

The **Media Manager** allows you to seamlessly upload, manage, and enhance your media files. You can also access open-source media libraries like Unsplash and Pexels from here.

Upload Media
------------

![](https://droip.com/wp-content/uploads/2023/03/Upload-Media.webp)

First up is the **Upload Media** Button. Upon clicking, the `Upload Media Window` will appear, offering two straightforward methods to upload your media:

1. **Drag and Drop**: Simply drag your desired media files into the designated area.
2. **Upload From Computer**: Click the button to open your computer’s file manager and choose the media you wish to upload.

The following media types are supported for uploading:

* Image
* Video
* Audio
* SVG
* Lottie

Home
----

![](https://droip.com/wp-content/uploads/2023/03/Home-6.webp)

In the **Home** section, you can access your entire media library. Utilize the Search field at the top to efficiently locate your desired files.

Select an image from this section to reveal customization options in a side panel to the right. Further details on these options are provided below.

### Image Crop & Edit

![](https://droip.com/wp-content/uploads/2023/03/Image-Crop-Edit.webp)

The **Image Crop & Edit** option opens the **Edit Media** window, which facilitates cropping and editing of images.

* **Crop**: Adjust the blue frame’s corners to define the desired cropping area.
* **Flip**: Horizontally or vertically flip the image.
* **Rotate**: Rotate the image by 90 degrees anti-clockwise with each click.
* **Aspect Ratio Type**: Modify the aspect ratio:
  + **Original**: Maintain the initial aspect ratio.
  + **Freeform**: Crop freely without restrictions.
  + **Square**: Achieve a 1:1 aspect ratio.
  + **Ratio**: Select ratios such as 4:3, 5:4, 3:2, 16:9, 1:1, and 4:1.
* **Revert to Original**: Restore the image to its original state.
* **Undo/Redo**: Reverse or redo actions.
* **Adjust & Filter**: Access the `Adjust` and `Filter` sections from the side panel on the right.
* **Add**: Save changes and insert the edited image into the canvas.

### Adjust

![](https://droip.com/wp-content/uploads/2023/03/Adjust.webp)

In the **Adjust** section, enhance your selected image using the following properties:

* **Exposure:** Increasing Exposure increases the amount of “light” in the image i.e. brightens the image.
* **Contrast:** Increasing Contrast will result in darker shadows and brighter highlights.
* **Saturation:** Increasing Saturation increases the intensity of the image’s colors.
* **Warmth:** Increasing Warmth will enhance warmer tones of the image like yellow, orange, and red.
* **Tint:** The Tint property recolors the entire image in a single color specified by you.
* **Highlight:** Increasing the Highlight brightens the lightest portions of the image.
* **Shadow:** Increasing Shadow darkens the darkest portions of the image and adds more depth.

### Filters

![](https://droip.com/wp-content/uploads/2023/03/Filter.webp)

The **Filters** section provides pre-made filters to enhance your images. Options include:

* Original
* Grayscale
* Sepia
* Invert
* Duo-tone
* Warm
* Cool
* Dramatic

📝 **Note:** Any edited image will be saved as a new image in the Media Library.

Additionally, right-clicking over any Media item in Home will give you the following options:

* **Get URL Link:** A handy option using which you can copy the URL of the selected Media.
* **Move to Trash:** Delete the item by moving it to the Trash folder.

My Files
--------

![](https://droip.com/wp-content/uploads/2023/03/My-Files.webp)

The My Files section may look similar to the Home section and also has some of the same features but that’s not all there is to it.

In this section, you will find only the media that you have uploaded. This includes all of the Images, Videos, and any other media types.

* **Search:** You can search through your assets using the input field that’s at the top of this section.
* **Filter:** Click on the Filter icon that’s beside the Search field to access filtering options. You can filter your media by its type i.e. Image, Video, Audio, SVG & Lottie. Also, note that you can filter multiple types at a time and a tick icon will appear beside the ones selected.
* **Sort:** You’ll find the Sort icon beside the Filter option. Click on this toggle to Sort your assets in ascending or descending order.

Clicking on any Image will once again make the options **Crop & Edit**, **Adjust,** and **Filters** appear on the right. And, right-clicking on a Media item will give you the options **Get URL Link** & **Move to Trash**.

Trash
-----

This folder is where all of the “deleted” items reside until you restore them or it gets permanently deleted.  To restore a media, simply right-click and select the Restore option. If not restored, these get permanently deleted from the trash in 30 days.

Image Library
-------------

The Image Library is where you can access the images from open-source libraries such as Unsplash and Pexels if connected using their respective [API Integrations](https://droip.com/docs/api-integrations/).

If connected, you can use the following options to find and filter their open-source media:

**Search**: Use the Search field to find keyword-specific images and videos.

**Library**: From the dropdown on the top-left select which library you want to browse. Options are Unsplash and Pexels.

**Media Type**: From the middle dropdown, choose what type of media type you want to browse. Options are Photos and Videos.

**Orientation**: From the last dropdown, choose which orientation of images you want to browse. Options are Orientation, Landscape, Horizontal, and Square.

To add an image, simply select one and click on **Add**. You’ll also see the usual options **Crop & Edit**, **Adjust**, and **Filters** appear on the right when you do.

You can also right-click on any image to find the **Get URL Link** option.

Icon Library
------------

![](https://droip.com/wp-content/uploads/2023/03/Icon-Library-1.webp)

As the name suggests, the Icon Library is home to a plethora of icons to choose from and add to your page.

**Category:** Click on the dropdown at the top to access the various icon categories available. By default, the **Default Icon** category should be selected but here you’ll also find the following options:

* Material Icons: When selected, these can be filtered using the following options which appear on the left sidebar:
  + Filled
  + Outlined
  + Round
  + Sharp
  + Two Tone
* Line Awesome Icons
* Mono Icons
* CSS Icons
* ZW Icons

**Search:** Use this field to search for a specific icon.

Select an icon to access the options on the right sidebar which include the following:

**Thumbnail:** First up, you’ll see a preview of the Icon you’ve selected followed by its name.

**Color:** Next up you’ll see the color options available for this icon. Click on one to select it.

**Code:** Here, you’ll find a read-only code editor containing its code and you can copy it by clicking on the copy icon.

Don’t forget to click on the Add/Update button to add the Icon to the page or apply your changes.

Clip-Path & Shape Editor
------------------------

![](https://droip.com/wp-content/uploads/2023/03/Clip-Path-Shape-Editor.webp)

The **Clip-Path & Shape Editor** empowers creative design with three distinct tabs:

1. **SVG Shapes**: Customize shapes from the Shape Library, with options to adjust fill, stroke color, and weight.
2. **Image Clip**: Crop images into desired shapes using preset options or uploaded images.
3. **Text Path**: Manipulate text path shapes, customize stroke properties, and adjust text positioning.

### SVG Shapes

Under SVG Shapes, on the right side panel, you’ll find the **Shape Library** containing various Shapes to choose from which you can also later customize to suit your needs.

Once you’ve chosen your shape it should appear on the Preview Pane. You can drag the shape’s vertices to adjust it and you can also hover over an edge and click to add more vertices.

On the right side panel you’ll find the following options:

* **Fill:** Set the color & the opacity of your shape from here.
* **Stroke Color:** Set the color & the opacity of your shape’s outline from here.
* **Stroke Weight:** Set the weight of the stroke by entering into the field that’s below the Stroke Color toggle.

### Image Clip

Using the Image Clip feature, you can crop an image to take a particular shape.

On the Preview Pane, you should be able to see the image you’ll be clipping along with the shape you selected overlaying this image.

You can choose from many preset shapes from the panel on the right-hand side.

**Change Image:** Click on this option to replace the current image with a different one. This will open the Home section of the Media Manager from where you can select any image of your choice.

**Upload Image:** Directly upload an image to clip into shape.

Once you’ve chosen the shape you want to clip your image into, you can drag its vertices to customize it and even add new vertices by clicking on any edge if needed.

### Text Path

Text Path is a really nifty feature that lets you customize the path your text will lie on.

On the Preview Pane, you’ll see the Text lying on a path and the shape of this path can be selected from the preset options available on the right. Options include:

* Line
* Wave
* Cubic S
* Cubic C
* Arc
* Quad

Once you have selected the shape of your path, you can customize it on the Preview Pane by dragging its vertices. And to change the default text simply double-click on it and start typing.

Following the Preset Shapes for Path, you’ll find the following customization options:

**Path Stroke:** By default, the Path Stroke is disabled meaning that the stroke cannot be seen but you can simply click on the eye icon to make it visible. Then you can set its

* Color
* Opacity
* Stroke Weight

**Vertical Offset:** Set the vertical gap between the Path Stroke and the text.

**Horizontal Offset:** Set by how much the text will shift to the right.

---

<!-- Source URL: https://droip.com/docs/transform/ -->

---

Transform

The Transform module is a powerful tool for creating captivating 2D and 3D animations, adding depth and motion to your web pages.

Head over to `Style Panel` > `Transform` on the right-hand side of your screen to start playing with this module.

Basic Transformations
---------------------

The Transform section offers four different types of transformation:

1. Move
2. Rotate
3. Scale
4. Skew

### Move

![move transformation](https://droip.com/wp-content/uploads/2023/09/Move.webp)

As the name suggests, the Move Transform lets you shift your element across the page without affecting any of the other elements.

* **X:** Move the element horizontally to the right.
* **Y:** Move the element vertically downwards.
* **Z:** Move the element forward or backward i.e. into or out of the page.

Similar to Rotate, you must apply 3D Transformation and set the [Perspective](https://droip.com/docs/transform/#:~:text=the%20top%20edge.-,3D%20Transformation,-Use%20the%20toggle) for Move Z to have any effect.

### Rotate

![Rotate transformation](https://droip.com/wp-content/uploads/2023/09/Rotate.webp)

Using Rotate Transform, you can tilt your element by any given angle.

* **X:** Rotate the element along the X axis or in other words horizontally.
* **Y:** Rotate the element along the Y axis or in other words vertically.
* **Z:** Rotate the element along the Z axis.

The two toggles below Z Rotate allow you to tilt the element 15 degrees clockwise or anti-clockwise respectively.

On its own, rotating along the X or Y axes will result in a flat, 2D Effect, and rotating along the Z axis will have no effect at all. To get a 3D effect, you’ll have to do the following:

1. Select the parent element which may be a div, section, etc.
2. Go to `Transform` and enable `3D Transformation`.
3. Set the `Child Perspective` to 1000.

Doing this should switch the Move effect to a 3D perspective instead of simply 2D.

### Scale

![scale transformation](https://droip.com/wp-content/uploads/2023/09/Scale.webp)

The Scale Transformation lets you increase or decrease the size of an element.

* **X:** Transform your element to have greater width.
* **Y:** Transform your element to have greater height.
* **Z:** Scale your element along the Z-axis. This effect works well when a parent element has children with varying Z values for either Move or Rotate. (More on how this works later in the documentation!)

💡 **Tip:** Click on the link icon to link X and Y values which will cause elements to scale proportionately.

You can also use the two buttons below the Z-axis toggle to proportionately scale your element to be bigger or smaller.

### Skew

![skew transformation](https://droip.com/wp-content/uploads/2023/09/Skew.webp)

Using the Skew feature you can stretch your element.

* **X:** Stretch your element along the x-axis.
* **Y:** Stretch your element along the y-axis.

Fun Fact, know that for Skew, 3D Perspective doesn’t affect any change.

Set Transformation Origin
-------------------------

![Set Transformation Origin](https://droip.com/wp-content/uploads/2023/09/Set-Transformation-Origin.webp)

You can define the point from which the transformation originates. By default, this point is at the element’s center. You can set the origin using the grid model or the input fields on the right.

* **Right:** Set the Origin’s distance from the left edge.
* **Top:** Set the Origin’s distance from the top edge.

3D Transformation
-----------------

![3D Transformation](https://droip.com/wp-content/uploads/2023/09/3D-Transformation.webp)

Enabling 3D Transformation is where the magic begins. It allows you to set the Perspective, which represents the 3D view on a 2D plane. This Perspective provides depth to 3D Compatible transformations.

Perspective can be set in two ways under the Distance section:

* **Self:** Applies to the element and its children. Distortion is relative to this element.
* **Child:** Applies to all child elements. Distortion is relative to the viewport.

### Self Perspective

To set the Self Perspective:

* Select the element you want to transform.
* Then, go to `Transform` > `3D Transformation` > `Distance`
* Set the value for **Self**.

As previously mentioned, this distortion will be relative to this element and because of this nature, Self Perspective works best when you’re transforming a single element.

### Child Perspective

Similarly, to set the Child Perspective:

* Select the parent element that contains the child elements you want to transform.
* Go to `Transform` > `3D Transformation` > `Distance`.
* Set the value for **Child**.

As you may know, this distortion is relative to the viewport. This means that the parent element acts kind of like a camera through which the elements are viewed.

In contrast to Self Perspective, Child Perspective is more realistic and is especially great when transforming multiple elements.

### Perspective Origin

Following this, you can set your Perspective’s origin, i.e. at which position the user is looking at the element. Similar to Transformation Origin, you can use the grid model to set this or use the input fields on the right to define your own values:

* **Left:** Set the Origin’s distance from the left edge.
* **Top:** Set the Origin’s distance from the top edge.

Scale Z
-------

Using the Scale Transformation, you scale an element along the X, Y, and Z Axes. But unlike Scale X and Y, the true effect of Scale Z is not as obvious on its own. But in the right setting, Scale Z is a highly powerful feature.

As mentioned earlier, you will notice its true effect when applied to a parent element that contains a group of child elements with varying Z values (for Move or Rotate).

### Scale Z Explained In Action

Let’s now go over exactly how you can make this feature work.

Consider a scenario where you have a Section containing a Container, which, in turn, holds three SVG Icons.

To grasp the concept, follow these steps:

1. **Child Perspective**: Begin by selecting the Section. Set its Child Perspective to 1000px. Achieve this by navigating to `Transform` > `3D Transformation` > `Distance`.
2. **Container Rotation**: Proceed to select the Container. To better visualize the Scale Z effect, rotate the Container horizontally using a 50px Rotate X setting.
3. **Icon Z-Move**: Apply the following settings to the three Icons within the Container:
   * Icon 1: Move Z by 10px
   * Icon 2: Move Z by 20px
   * Icon 3: Move Z by 30px
4. **Container Scale Z**: Return to the Container and set its Scale Z value to 2. Observe how the effect appears to double the three Move Z values.

Basically, increasing or decreasing the Scale Z of a parent element will increase or decrease all varying Z values of the child elements be it Move Z or Rotate Z.

Adding 3D Animation Effect on Hover
-----------------------------------

Transform offers exciting possibilities for interactive animations. Let’s create a turning effect on images when hovered over:

### Setup Your Page

1. Design your page by starting with a `Section` element.
2. Inside the Section, insert a `Flex` element with **3 Flex Tracks**.
3. Add an `Image` element to each Flex Track and choose the media you want to use for each Image. Use the `Add From Media` button for this purpose.
4. Set the Flex’s alignment to **Center** and justify it to **Space Evenly**.

### Transform Your Elements

Now, let’s turn our images so that they face away from the user. Do the following to achieve this:

1. Select the Section and go to `Transform`.
2. Enable **3D Transformation** and set the **Child Perspective** to 1000px.
3. Select the first **Flex Track** and rotate it vertically by 60 degrees. You can do this by going to `Transform` > `Rotate` and setting the Y value to 60.
4. Repeat the same for the other two as well.

### Animate on Hover

Your images should now appear turned to one side. Let’s add the animation:

1. Select the first **Flex Track** again.
2. From the `Class & Sub-class` section on the right, click on the expansion icon to reveal the `States Menu`.
3. While the Flex Track is selected, switch to the **Hover** state.
4. Within the Transform settings, set **Rotate Y to 0**.
5. Repeat these steps for the other two Flex Tracks.

### Get a Smoother Transition

The images should now turn towards you when hovered over. However, the animation might look abrupt. Here’s how to fix it:

1. Once more, select the first flex track.
2. Then, from the Style Panel, go to `Transition`.
3. Click on the `+` icon to add a new Transition and from the new pop-up window set the type as **Transform**, Duration to **300ms**, and Timing Function as **Ease**.
4. Now repeat the same for the other two as well.

And this is just one example of 3D Animation and you can apply the same concept to add any kind of animation to any elements of your choice.

---

<!-- Source URL: https://droip.com/docs/link-block/ -->

---

Link Block

A `Link Block` in Droip is a useful element that can turn any other element, such as an image or text, into a clickable link. It functions similarly to the Div block but comes with the added functionality of creating a link.

Adding a Link Block
-------------------

To add a Link Block, follow these simple steps:

1. Open the `Elements Panel` in the left sidebar.
2. Drag the `Link Block` element onto your page.

Once you have added the Link Block, you can easily add other elements inside it, with the exception of other links.

Adding Elements Inside the Link Block
-------------------------------------

![](https://droip.com/wp-content/uploads/2023/03/Adding-a-Link-Block.webp)

To include an element inside the Link Block, follow these steps:

1. Drag any element from the `Elements Panel`.
2. Drop the element inside the `Link Block`.

Link Block Settings
-------------------

The Link Block offers various settings to customize its behavior and appearance:

### Layout

Link Blocks can be used to create layouts and structures similar to Div blocks. Click on the Link Block, and you can choose your preferred grid layout from the element’s inline editor.

### Set the Link Type

To set the link type of the Link Block, follow these options:

* **Web Address:** Enter the URL of the page you want to link to in the field below. Tick the checkbox to enable **Open in New Tab**.
* **Email:** To link an Email, enter the Email address and the Subject in the available fields.
* **Phone Number:** Enter the Phone Number you want to link along with its country and area code in the following field.
* **Page:** Select the Page you want to link from the following drop-down list and tick the checkbox for it to **Open in New Tab**.
* **Section:** Type in the Section Id in the text field below to link to a particular Section that is on this page.
* **Pop-up:** Select the Pop-up you want to link from the following dropdown list.

**Open in New Tab:** Enable this option to open your link in a new tab when clicked.

**Rel:** The “Rel” option is short for “relationship” and is an attribute used in HTML to specify the relationship between the element and the linked resource.

Overall, the Link Block in Droip allows you to create clickable links from any other element on your page. By using this element, you can create more interactive and engaging designs for your website or application.

---

<!-- Source URL: https://droip.com/docs/borders/ -->

---

Borders

The Borders section in Droip’s Style Panel allows you to add and customize borders or outlines around elements.

![Borders options in Droip Style panel](https://droip.com/wp-content/uploads/2023/03/borders.webp)

Border
------

A border consists of lines drawn around an element’s edge, enclosing its content. You can adjust the following options:

* **Size:** Define the size of the border and its unit.
* **Color:** Select the color of the border.
* **Radius:** Set the corner radius for rounded corners.
* **Individual Radius:** Click on the small border icon beside the Radius input field to customize corner radius individually for each corner.

![Stroke Border](https://droip.com/wp-content/uploads/2023/09/Border.webp)

### Individual Border

Droip’s border control lets you individually style each side (top, right, bottom, left) of an element’s border. You can:

* Click on each side of the border icon to activate/deactivate it.
* Apply different border widths, colors, or styles to each side independently.

This is especially handy when you want subtle detailing like a bottom-only underline effect or asymmetrical card designs.

**💡Tip:** Use this feature to set one edge of an element a lighter color than the other three to create a 3D effect as shown in the image above.

### Visibility

Click on the eye icon to disable/enable the visibility of the border.

Outline
-------

![Stroke outline](https://droip.com/wp-content/uploads/2023/09/Outline.webp)

Outlines fully enclose an element and are drawn outside its edges. Customize your outline with the following options:

* **Size:** Define the size of the outline and its unit.
* **Color:** Select the color of the outline.
* **Offset:** Set the space between the outline and the border/edge. Click on the ellipsis icon to access this property.
* **Visibility:** Toggle the outline’s visibility using the eye icon.

Styles
------

![Borders Styles in Droip](https://droip.com/wp-content/uploads/2023/03/style-1.webp)

You can choose from various styles under the **Border** and **Outline** Tabs:

* Solid
* Dashed
* Double
* Dotted
* Outset
* Inset
* Grooved
* Ridge
* None

Use Cases
---------

Borders and outlines can be used creatively to enhance your designs:

* **Emphasizing Elements:** Use bold borders to draw attention to specific elements.
* **Creating Depth:** Apply subtle outlines to give elements a sense of depth and separation.
* **Highlighting Interactivity:** Add dynamic transitions to elements on hover or focus states.

Using Borders For Animated Transitions
--------------------------------------

You can use borders to emphasize elements during Hover or Focus states. Here’s an example involving an Image element but this can be applied to other elements too:

1. Select your **Image** element and from `Style Panel` > `Borders`, set its border size to 8px and radius to 100%. Also, select a color for your border from here.
2. Then, go to `Style Panel` > `Class & Sub-Class` > `States Menu`. (If you don’t see the States Menu, don’t forget to click on the Expand icon on this section’s top-right.) and select the **Hover** state.
3. Next, go back to the Borders section, and set the border size to 0px and the radius to 0%.

Now set up a Transition for smoother border appearance:

1. Go to `Style Panel` > `Effects` > `Transition` and click on the `+` icon to add a new transition.
2. On the new pop-up window, click on the dropdown on the top-left and select the `Border Radius` option as the transition property.
3. Set the Duration as **300 ms** and the Timing Function as **Ease** and you’re done!

Click on the `Preview` icon which you’ll find on the right side of the Top Bar to see this transition in motion.

Best Practices
--------------

For effective design with borders and outlines, consider these best practices:

* **Consistency:** Maintain consistent border widths, colors, and styles for a cohesive design.
* **Contrast:** Ensure sufficient contrast between borders and backgrounds for visual appeal.
* **Accessibility:** Use contrasting colors for borders to aid users with visual impairments. Also, ensure sufficient contrast between elements and background.

---

<!-- Source URL: https://droip.com/docs/shadow/ -->

---

Shadow

Shadows are a powerful tool to add depth and emphasis to your elements. You can find the Shadow feature in the Style Panel on the right side of the Droip interface.

![Add shadow in Droip](https://droip.com/wp-content/uploads/2023/09/Shadow.webp)

Adding and Managing Shadows
---------------------------

**Add Shadow:** Click on the `+` icon to add a new Shadow layer. A new Shadow item will be added to the list.

![Adding and Managing Shadows](https://droip.com/wp-content/uploads/2023/09/Adding-and-Managing-Shadows.webp)

**Reorder Shadows:** Use the `four-dot` icon to drag and rearrange the order of Shadow layers.

**Visibility:** Toggle the visibility of the Outer Shadow by clicking the `eye` icon on the right.

**Remove Shadow:** Click on the `dash` icon to remove the selected Shadow.

Shadow Settings
---------------

![Shadow Settings](https://droip.com/wp-content/uploads/2023/09/Shadow-Settings.webp)

Customize your Shadow settings with the following options:

* **Shadow Type:** Choose between Inner Shadow (inside the element) and Outer Shadow (outside the element).
* **X:** Define the shadow’s horizontal offset i.e. how much the shadow will shift to the right compared to the element.
* **Y:** Define the shadow’s vertical offset i.e. how much the shadow will shift downwards.
* **Blur:** Define the sharpness or blurriness of the shadow’s edges.
* **Spread:** Set the extent to which the shadow spreads outward.
* **Color:** Set your shadow’s **Color** and **Opacity**.

Shadow Presets
--------------

Instead of customizing your own shadow, you can save time by using a **Shadow Preset**!

![Shadow Presets](https://droip.com/wp-content/uploads/2023/09/Shadow-Presets.webp)

To access Shadow Presets:

1. Click the `Show` button at the bottom of the Shadow section.
2. Choose from a range of preset shadows.
3. Select a preset to apply it instantly.

Saving Custom Shadows
---------------------

![Saving Custom Shadows](https://droip.com/wp-content/uploads/2023/09/Save-Custom-Shadows.webp)

Create and save your own custom Shadow presets:

1. Click the `+` icon beside the last preset option.
2. In the new window, name your preset and click `Add`.
3. This saved preset can be reused across different elements.

Using Shadow For Animated Transitions
-------------------------------------

Leverage shadows to emphasize elements in various states, like Hover mode with transitions:

1. Start by adding an Outer Shadow to your element with an opacity of 30% from `Style Panel` > `Shadow`.
2. Go to `Style Panel` > `Class & Sub-class` > `States Menu` and select the **Hover** state.
3. Increase the opacity of the shadow to 40% for the Hover state.
4. While your element is selected, navigate to `Style Panel` > `Transition` and add a new Transition.
5. Set the transition type as **Box Shadow,** with a duration of 300 ms and a timing function of **Ease**.

---

<!-- Source URL: https://droip.com/docs/role-manager/ -->

---

Role Manager

In Droip, you can manage user roles and set different access levels for each role.

![Role Manager in Droip](https://droip.com/wp-content/uploads/2023/02/set-different-access.webp)

Here is a brief overview of the different roles and access levels:

1. **Administrator**: This is the highest level of access and allows users to manage all aspects of the website, including adding and deleting users, installing and configuring plugins and themes, and creating and editing content.
2. **Author**: This role allows users to create and edit their own content, but they cannot publish it without approval from a higher-level user. But you can manually set their access levels.
3. **Contributor**: This role allows users to create and edit their own content, but they cannot publish it without approval from a higher-level user.
4. **Editor**: This role allows users to create and edit content, as well as publish content created by other users.
5. **Subscriber**: This role is the lowest level of access and only allows users to view content on the website.

As for the different access levels, they are:

![Different Access Levels in Droip Role Manager](https://droip.com/wp-content/uploads/2023/02/different-access-levels.webp)

1. **No Access**: Users with this level of access have no access to use Droip or its content.
2. **Full Access**: Users with this level of access have complete access to all aspects of the Droip plugin, including content.
3. **Content Only**: Users with this level of access can only access and edit the content on the site.
4. **View Only**: Users with this level of access can only view the Droip pages, but they cannot edit them.

---

<!-- Source URL: https://droip.com/docs/interaction/ -->

---

Interactions

What is an Interaction?
-----------------------

An **interaction** is any kind of visual movement or response that happens between a user and a website.

This could include an element sliding into view, growing on hover, or changing position as the user scrolls.

In Droip, an interaction is made up of two components:

**Trigger** – What initiates the animation (e.g., click, hover, scroll).  
**Animation** – The visual effect that is performed in response.

Types of Triggers
-----------------

Triggers determine **when** an animation starts. In Droip, there are two categories of triggers:

### 1. Element Triggers

![Droip Element Triggers](https://droip.com/wp-content/uploads/2023/03/droip-element-triggers.webp)

These are tied to specific elements on your page and activate when users interact with those elements.

**Available Element Triggers:**

* **Mouse Click (Tap)** – Runs the animation when the element is clicked.
* **Mouse Hover** – Runs the animation on hover.
* **Mouse Move Over Element (Continuous)** – Runs and continues the animation as long as the mouse moves over the element.
* **While Element is Scrolling** – Continuously runs the animation based on the element’s position while it scrolls through the viewport.
* **Scroll Into View** – Starts the animation when the element enters the viewport while scrolling.

You can trigger an animation **on the same element** or on a **different one** based on your setup.

### 2. Page Triggers

![](https://droip.com/wp-content/uploads/2023/03/droip-page-triggers.webp)

These are activated by changes in the overall page state.

**Available Page Triggers:**

* **While Page is Scrolling** – Activates when the page is being scrolled.
* **Page Load** – Activates as soon as the page loads.
* **Scroll Into View** – Activates when a specific element becomes visible while scrolling.
* **Page Scrolled** – Activates when the user scrolls either up or down.

Step 1. Setting Up the Trigger
------------------------------

For an **Element Trigger**: Select the element (or group of elements), then click the `+` icon next to `Interactions` on the style panel.

For a **Page Trigger**: In the **Layers** panel, select `Page`, then click the `+` icon next to `Interactions` on the style panel.

Once added, you’ll get specific configuration options depending on the trigger type.

![Configuring the Interactions Triggers in Droip](https://droip.com/wp-content/uploads/2023/03/Configure-the-trigger.webp)

For example, with **Mouse Click (Tap)**, you can set different animations for the **first** and **second** clicks.

Step 2. Setting Up the Animation
--------------------------------

After defining the trigger, you can proceed to define the **response** (animation) that occurs when the trigger is activated.

**Response Options:**

* **Set New** – Opens the **Timeline Editor** to create a custom response using precise controls.
* **Library** – Choose from Droip’s preset animation effects.
* **Text Animation**s – Available when targeting a text element, offering preset animation styles for text. [Learn more on Text Animations](https://droip.com/docs/text-animations/).

### Using the Animation Library

The **Library** offers ready-made animation presets, including: Fade, Slide, Light-Speed, Flip, Bounce, Swing, Tada, Wobble, and more.

Each animation comes with configuration options like:

* **Direction** – In / Out
* **From** – Left / Right
* **Duration** – How long the animation lasts
* **Delay** – Time before animation starts
* **Loop** – Repeat animation continuously
* **Repeats** – Number of times to repeat
* **Fill Mode** – Retain or reset animation state after it ends
* **Easing** – Animation speed curve (e.g., linear)

### Custom Animations with the Timeline Editor

![Custom Animations with the Timeline Editor](https://droip.com/wp-content/uploads/2023/03/Custom-Response1.webp)

Click `Set New` to launch the Timeline Editor. The **Timeline Editor** lets you create a custom response using precise controls.

**How it works:**

Target Elements appear on the left. To add one, select the target element from the canvas.

Choose an action. Action icons are located above the Timeline and are basically style attributes like color, move, scale, size, etc., that you can alter for your target element in response to the trigger.

Similarly, when you hover your mouse over the timeline, a vertical blue line with a plus `+` icon will appear. This indicates where a new animation action can be inserted. Clicking the plus icon opens a dropdown with various animation actions you can apply, such as Move, Scale, Rotate, Opacity, and more.

You can also choose Variable Mode from this list to assign it as an action. This allows you to animate a property based on a variable, perfect for creating responsive animations that adapt to user-defined or dynamic values.

Once added, the new action will appear as a block on the timeline where you can further adjust its start and end time, as well as edit its properties.

**Editing:**

Click on any timeline action to select it.

Drag its start/end points to control when it happens. Or you can specify the value in percentage at the bottom of the timeline. For example, if you set:

* Start: 2%
* End: 95%

It means the animation will begin slightly after the animation starts (at 2%) and finish just before the end (at 95%). This gives you precise control over the timing of each animation within the overall interaction.

Set keyframe values for properties like size, position, or opacity.

Example: If you’re animating the opacity of an element:

* At Start (2%), set the opacity to 0 (fully transparent).
* At End (95%), set the opacity to 1 (fully visible).

This will create a smooth fade-in effect that happens between 2% and 95% of the animation timeline

**Tools:**

* **Smoothing** – Adjust how fluidly the animation plays.
* **Viewport Only** – Limit animation to when the element is visible.

**Example Workflow:**

To animate an element’s size during scroll:

1. Select the target element.
2. Go to `Interactions` **→** `+` **→** `While Page is Scrolling`.
3. In the Response panel, click the `Size` action.
4. Drag the animation block in the timeline.
5. Adjust scroll percentages and size keyframes.

You can also click on a target to:

![Custom Animations with the Timeline Editor in Droip](https://droip.com/wp-content/uploads/2023/03/Custom-Response2.webp)

* Apply to Class – Apply animation to all elements with the same class.
* Change Target
* Duplicate Target
* Delete Target

### Trigger Animations on Specific Breakpoints

![Trigger Animations on Specific Breakpoints in Droip](https://droip.com/wp-content/uploads/2023/03/Specific-Breakpoints.webp)

You can control which devices an animation should run on.

1. In the **Interactions** panel, once you’ve added an animation, click the **three-dot icon** next to the **Response** label.
2. Select Breakpoints from the dropdown that will appear.
3. **Select the breakpoints (devices)** where you want the animation to apply.

This ensures your animation only runs on selected screen sizes, helping you create responsive and performance-optimized experiences.

### Apply Animation to All Elements with the Same Class

![Apply Animation to All Elements with the Same Class](https://droip.com/wp-content/uploads/2023/03/Same-Class.webp)

To reuse the same interaction across multiple elements sharing a class:

1. In the **Interactions** panel, once you’ve added an animation, click the **three-dot icon** next to the **Response** label.
2. Select **Breakpoints** from the dropdown that will appear.
3. Toggle the option **Apply to Class**.
4. Select the **class** you want the animation to apply to.

Now, all elements with that class will automatically inherit the same animation for the same interaction event.

This is especially useful for repeated components like cards, buttons, or list items, where you want consistent animation behavior across the board, without having to manually animate each element.

Custom Timing Editor
--------------------

![Custom Timing Editor in Droip](https://droip.com/wp-content/uploads/2023/03/Custom-Timing-Editor.webp)

The **Custom Timing Editor** lets you define your own easing curves and animation pacing.

With the Custom Timing Editor, you can define a custom easing curve and set keyframe values to create a more natural and dynamic animation.

### Timing Function Styles:

* **Ease In**: This style starts the animation slowly and gradually speeds up. This is useful for creating a sense of acceleration.
* **Ease Out**: This style starts the animation fast and gradually slows down. This is useful for creating a sense of deceleration.
* **Ease Both**: This style starts the animation slow, speeds up in the middle, and then slows down again. This is useful for creating a more natural and dynamic animation.

**Using the Graph:**

* Create curves by adjusting keyframe values:  
  + **Bottom curve = slow start**
  + **Top curve = fast start**
  + Add peaks/troughs for springy effects

You can also:

* Adjust the **duration** by dragging endpoints
* **Preview** animations before publishing

By experimenting with different styles, you can create unique and engaging animations that will make your website stand out.

Here’s how to use the graph to create different timing function styles:

1. **Ease In**: To create an “Ease In” style animation, start by setting the keyframe values at the bottom of the graph. This will create a slow start to the animation. As you move toward the middle of the graph, gradually increase the keyframe values to create a sense of acceleration.
2. **Ease Out**: To create an “Ease Out” style animation, start by setting the keyframe values at the top of the graph. This will create a fast start to the animation. As you move toward the middle of the graph, gradually decrease the keyframe values to create a sense of deceleration.
3. **Ease Both**: To create an “Ease Both” style animation, start by setting the keyframe values at the bottom of the graph for a slow start, then gradually increase the keyframe values to create a sense of acceleration. As you reach the top of the graph, gradually decrease the keyframe values to create a sense of deceleration.

---

<!-- Source URL: https://droip.com/docs/section/ -->

---

Section

The **Section** element in Droip allows you to structure your web page effectively by dividing them into distinct sections, each with its own unique purpose and content.

![Section element in Droip](https://droip.com/wp-content/uploads/2023/02/Section.webp)

In Droip, a Section represents a self-contained block of content that is thematically related. It is typically used to organize content into logical groupings, each having a specific focus or topic. Each Section can have its own heading, making it easy for visitors to identify and understand the purpose of the content within.

Examples of Section Usage:
--------------------------

* **Hero Section**: Start your webpage with an impressive Hero Section that grabs visitors’ attention and introduces your core message or product.
* **Features Showcase**: Create a Features Section to highlight the key features and benefits of your product or service.
* **Testimonials**: Use a Testimonials Section to showcase reviews and feedback from satisfied customers.
* **Contact Information**: Include a Contact Section with your address, contact details, and a contact form.

Adding a Section
----------------

![Adding a Section in Droip](https://droip.com/wp-content/uploads/2023/02/Adding-a-Section.webp)

To add a Section element to your Droip web page, follow these simple steps:

1. Open the Droip editor and navigate to the `Insert` > `Elements`Panel.
2. Look for the `Section` element and drag it onto your page canvas.
3. Customize the section’s appearance, such as background color, padding, and alignment, using the built-in **Style Panel**.

Structuring Your Web Page with Section Elements
-----------------------------------------------

To maintain a cohesive and well-organized website structure, follow these best practices:

* Use multiple Section elements to break down your page into meaningful segments.
* Within each Section, add content elements such as text, images, videos, and buttons to convey your message effectively.
* Experiment with different layouts and arrangements to create an engaging user experience.

Style a Section
---------------

The Section element in Droip is highly flexible and can be styled according to your preferences. You can:

* Set the background color or add background images to match your website’s theme.
* Adjust padding and margins to control the spacing within the section.
* Define custom heights to make certain sections stand out.

To learn more about styling options in Droip, refer to the [Style Panel](https://droip.com/docs/style-panel-overview/).

---

<!-- Source URL: https://droip.com/docs/typography/ -->

---

Typography

Typography is the technique of arranging type to make words readable and visually pleasing. To adjust the Typography of any element, go to `Style Panel` > `Typography`.

Basic Settings
--------------

![Basic Typography Settings](https://droip.com/wp-content/uploads/2023/03/Basic-Settings-1.webp)

Here, you can change the Font, Font Size, Alignment, and more. So let’s go over each feature one by one.

**Font:** Choose the font style from the drop-down list to define the visual identity of your text.

**Font Size:** Adjust the font size to enhance readability and balance within your design.

**Font Weight:** Select the font-weight or “boldness” of your text. Keep in mind that the weight will depend on the font style selected.

**Line Height:** Set the line height to determine the spacing between lines of text, contributing to improved readability.

**Letter Spacing:** Control the horizontal spacing between each letter, optimizing legibility and aesthetic appeal.

**Color:** Choose the foreground color of your text and text decorations, ensuring cohesive and visually pleasing designs. Learn more on [Color Settings](https://droip.com/docs/color-settings/).

**Text Alignment:** Specify text alignment for optimal presentation. Options include left, center, and right alignment.

Advanced Typography
-------------------

![Advanced Typography in Droip](https://droip.com/wp-content/uploads/2023/03/Advanced-Font-Editor-3.webp)

Following the settings mentioned above is a button called **Advance Typography**. Clicking on this should give you access to more advanced text formatting options.

**Alignment:** In addition to the standard left, center, and right alignments, the Advanced Font Editor offers the `Justify` option. This aligns both edges of each line of text with both margins, enhancing visual consistency.

**Decoration:** Emphasize text using decorations. Options include:

* **No Decoration:** Opt for simplicity by setting no decoration.
* **Bold:** Change your text weight to bold for emphasis.
* **Italic:** Italicize your text.
* **Underline:** Underline your text.
* **Line-through:** Strike a line through your text.
* **Overline:** Overline your text.

Text Stroke
-----------

![Text Stroke in Droip Typography](https://droip.com/wp-content/uploads/2023/03/Text-Stroke.webp)

Outline your typography using this option.

**Width**: Define the Stroke’s width.

**Color**: Set the Stroke’s color.

**Opacity**: Set the Stroke color’s opacity.

Paragraph
---------

### Clamp

This feature allows you to define the Font Size as a number between an upper and lower bound. It requires the three following parameters. It ensures that the font size remains within a specific range, providing flexibility and responsiveness in your design.

* **Base**: This is the preferred font size value that will be used when it falls within the specified range.
* **Min**: This is the minimum font size value. If the base value is smaller than the minimum value, the minimum value will be used.
* **Max**: This is the maximum font size value. If the base value is larger than the maximum value, the maximum value will be used.

### Character Unit

Set a container width value to constrain horizontal text span. This introduces line breaks after reaching the specified limit, enhancing readability.

### Word Break

Define where the line breaks appear when the text overflows its content box.

* **Normal:** Use the default Word Break rule.
* **Keep-all:** Prevent word breaks for Chinese/Japanese/Korean text. For other languages, Word Break behaves the same as in “Normal”.
* **Break-all:** Allows word breaks at any character (except for CJK text).
* **Break-word:** Randomly breaks words to prevent overflow.

### Truncation

Define text behavior when it overflows its container:

* **Clip:** Overflowing text is hidden.
* **Ellipsis:** Overflowing text is replaced with an ellipsis (“…”).

### Indentation

Control text-indent for space before the text:

* **Text-Indent:** Define how much space you want to add before the first line of text.
* **Text-Indent Left:** Define how much space you want to add on the left side of each line.
* **Text-Indent Right:** Define how much space you want to add on the right side of each line.

### Orientation

Set text orientation for vertical writing mode:

* **Mixed:** Default value. Characters of horizontal scripts are rotated 90 degrees, clockwise.
* **Upright:** Horizontal script characters, as well as vertical script glyphs, both remain upright but in a vertical script.

### Writing Mode

Enable vertical mode for your block of text from here. Options include Unset, RTL, and LTR.

* **Unset:** Click on this to disable vertical mode.
* **RTL (Vertical-rl):** LTR scripts will flow from top to bottom vertically with the next line positioned from the left of the previous. And RTL scripts will flow top to bottom vertically but the next line starts from the right of the previous.
* **LTR (Vertical-lr):** LTR scripts will flow from top to bottom vertically with the next line positioned from the right of the previous. And RTL scripts will flow top to bottom vertically but the next line starts from the left of the previous.

OpenType Feature
----------------

![OpenType Feature in Droip](https://droip.com/wp-content/uploads/2023/03/Open-Type-Feature.webp)

Utilize OpenType font features to enhance character styles:

### Letter Case

**Case:** Select the Letter Case you want your text to be. Options include the following:

* **None:** Keep default case.
* **Uppercase:** Transform all letters to uppercase.
* **Lowercase:** Transform all letters to lowercase.
* **Capitalize:** Capitalize initial letters.
* **Small Caps:** Uppercase letters with the height of lowercase letters.
* **All Small Caps:** All letters are transformed to uppercase but they are all smaller than the usual uppercase letters.

**Case-Sensitive Forms:** Enable this to allow certain characters to be shifted to better suit the case defined.

**Capital Spacing:** Enable this to allow spacing adjustments for capital letters.

### Numbers

**Styles:** Define numeral styles, options include:

* **None:** Default numeral style.
* **Uppercase:** Numerals are of the same height (Lining).
* **Lowercase:** Numerals can descend below the baseline (Old Style).

**Position:** Use Position to define subscript and superscript.

* **Subscript:** Numbers placed below the baseline.
* **Normal:** Default value. Numbers appear on the line.
* **Superscript:** Numbers placed above the baseline.

**Fractions:** Enable this to allow fractional glyphs to appear in your text.

### Letterforms

Control the use of Ligatures in your text block.

* **Ligatures:** Allow combined letters or glyphs to replace separate ones, enhancing spacing and readability. A common example of a Ligature is “fi”.
* **Rare Ligatures:** Enable rare ligatures for unique character combinations. Unlike Common Ligatures, Rare Ligatures are an unusual combination of letters, usually for the purpose of being eye-catching.

### Stylistic Sets

Stylistic Sets make the use of a font’s alternate glyphs so much easier and remove the need to manually replace each occurrence of a character with the desired alternate.

* **Stylistic Set 1:** Enable the first Stylistic Set.
* **Stylistic Set 2:** Enable the second Stylistic Set.
* **Stylistic Set 3:** Enable the third Stylistic Set.

### Horizontal Spacing

Fine-tune letter spacing using kerning data for balanced typography.

* **Kerning Pairs:** Kerning is a number by which the default spacing should increase or decrease. Enable this feature to apply Kerning.

### More Features

The following features are related to Fractions. With these enabled, you can use special fractional glyphs contained in an OpenType font.

* **Fractional Denominators:** Enable to allow the use of fractional denominator glyphs i.e. glyphs that are stylized according to the size and position of a denominator.
* **Fractional Numerators:** Enable to allow the use of fractional numerator glyphs i.e. glyphs that are stylized according to the size and position of a numerator.

Units in Typography
-------------------

Working with typography involves various types of units for length, color, and more. To understand these units, refer to our [Values and Units](https://droip.com/docs/values-and-units/) documentation.

---

<!-- Source URL: https://droip.com/docs/collection-element/ -->

---

Collection Element

Collections are a powerful way to fetch dynamic data to showcase on your website. Popular website pages that you can create using this element are Blog Archive Pages, Author List Pages, Documentation Archive Pages, and more!

Using Droip’s **Collection** element, you can easily narrow down the exact scope of the data you want to fetch through various criteria like Collection Type, Post Type, and Taxonomy! Depending on the structure of your website, the options listed within these types differ as they are also fetched dynamically.

How to Add a Collection
-----------------------

To add a Collection to your website, follow these steps:

1. From the Left Sidebar, go to `Insert` > `Elements`.
2. Scroll down to the `Advanced` section.
3. Drag & drop the `Collection` element onto your canvas.

Collection Types
----------------

![Collection List settings in Droip](https://droip.com/wp-content/uploads/2023/03/Collection-Source.webp)

From the Collection Settings, you can define the scope of the data you want fetched and apply filtering, sorting, and other customizations. To access this, click on the Collection icon on the inline editor.

The first criterion you can set is the **Collection Source**. Here you’ll find the following options:

1. **Post**: Choose Post Collection if you want to fetch content from various Post Types such as Blog Posts, Pages, Custom CSS, etc.
2. **Terms**: Choose Terms Collection if you want to fetch the Categories, Tags, etc that your website content is organized by.
3. **Users**: Choose User Collection to fetch user data saved on your website.

Once you’ve selected your Collection Type, you can then configure the specific settings for that type.

Post Collection Settings
------------------------

The first Collection option is Post. The Post Collection option extends beyond typical Blog Posts. In WordPress, various content types fall under the Post umbrella, including Pages, Attachments, and Custom CSS, among others.

### **Post Type**

Once you set your Collection as Post, you can then go on to choose these specific Post Types. These options will vary based on the structure of your website.

### **Inheritance**

Posts can be inherited. You can do so by ticking the **Parent** checkbox.

### List Items Layout

Select the number of columns you want the Collection to consist of, ranging from 1 to 5 Columns.

### Filter

![Collection Filter settings in Droip](https://droip.com/wp-content/uploads/2023/03/Filter-1.webp)

Set the filter method and criteria for the data. You can filter by:

* **Date**: Define a specific period of time using start and end dates.
* **Category**: Display data from a specific category or filter out data from a specific category.
* **Author**: Show data from a specific author or exclude data from that specific author.

To add a filter, click on the + icon that’s in this section’s top right corner. A new window called **Add Filter** should appear from where you can select the Method and other conditions. You can add multiple filters like this.

To edit or delete a filter, use the ellipsis icon next to each filter.

### Sorting

![Add sorting of collection](https://droip.com/wp-content/uploads/2023/03/Sorting.webp)

Specify the conditions to sort the Items by setting the **Method** and **Order**. From Method, you can select either Ascending or Descending. And for Order, you can choose which Attribute to sort according to.

To sort, click on the + icon that’s in the top right corner. A new window called **Add Sorting** will appear from where you can set the Method and Order.

To edit a Sorting, click on the three-dot icon that is beside each of them and choose the Edit option. You can also delete the Sorting by clicking on the three-dot icon again and selecting the delete option.

### Items Pagination

![Items pagination of Collection items in Droip ](https://droip.com/wp-content/uploads/2023/03/Item-Pagination.webp)

Enable Items Pagination to limit the number of items displayed on each **page**. Once enabled, you will be able to set the following:

* **Items Per Page**: Set the maximum number of items to display on each page.
* **Page Preview**: Set the default page to preview.

These settings will be automatically reflected inside the previously empty Pagination Wrapper.

Comment Collection Settings
---------------------------

Similarly, ‘Comments’ are another type of content that you’ll often find on websites.

### **Comment Type**

If you’ve selected Comment as your Collection, you can then go on to choose the Comment Type i.e. which set of comments you want to fetch.

Depending on your website’s structure and what’s installed on it, there can also be more than one Comment Type! Examples include Blog Post Comments, Product Reviews, etc.

### **Inheritance**

Since comments are automatically inherited, nested comments can also be showcased easily.

### Filter

Set the filter method and criteria for the Comments. You can filter by:

* **Date**: Define a specific period of time using start and end dates.
* **Status**: Show or filter out comments with a specific status.
* **Author**: Display comments from a specific author or exclude ones from that specific author.

To add a filter, click on the + icon that’s in this section’s top right corner. A new window called **Add Filter** should appear from where you can select the Method and other conditions. You can add multiple filters like this.

To edit or delete a filter, use the ellipsis icon next to each filter.

### Sort

Specify the conditions to sort the Comments by setting the **Method** and **Order**. From Method, you can select either Ascending or Descending. And for Order, you can choose which Attribute to sort according to.

To sort, click on the + icon that’s in the top right corner. A new window called **Add Sorting** will appear from where you can set the Method and Order.

To edit a Sorting, click on the three-dot icon that is beside each of them and choose the Edit option. You can also delete the Sorting by clicking on the three-dot icon again and selecting the delete option.

### **Items Pagination**

Enable Items Pagination to limit the number of items displayed on each **page**. Once enabled, you will be able to set the following:

* **Items Per Page**: Set the maximum number of items to display on each page.
* **Page Preview**: Set the default page to preview.

These settings will be automatically reflected inside the previously empty Pagination Wrapper.

Term Collection Settings
------------------------

Lastly, we have Terms. Terms can be anything from Categories to Tags. For this, you can select the following:

### **Post Type**

As mentioned previously, a Post Type encompasses many forms of content in WordPress. Here, you’ll find the options for Posts, Pages, and more.

### **Taxonomy**

In WordPress, Taxonomy is a grouping mechanism used to organize content. Examples include Categories, Tags, etc. You can also create custom Taxonomies for every Post Type.

The options in Taxonomy will differ based on the Post Type selected as each Post Type has a different set of Terms.

### **Inheritance**

Terms can also be inherited. You can do so by ticking the **Parent** checkbox.

Collection List Content
-----------------------

After you’ve configured the Collection element settings, your Collection List will be populated by this content dynamically. This is because the elements that make up a Collection Item have been set up by default to dynamically retrieve the information from the CMS itself.

![Connect elements to dynamic content fields](https://droip.com/wp-content/uploads/2023/03/Collection-list-content.webp)

You can edit these settings by clicking on any one of these elements and opening its **Dynamic Content Settings** from their inline editor as shown in the image above. Here, you can choose the Type of Content in your data set you want to retrieve as well as specify its Value.

### Static and Dynamic Elements in Collection

You can have both static and dynamic elements in your Collection List:

**Static Elements**

Static elements remain the same for all Collection Items. Simply drag and drop them from the Elements Panel into the collection, and they will be static by default.

**Dynamic Elements**

Certain Static Elements can be set up to fetch and show Dynamic Data. All you have to do is select it and click on the Data Collection icon to configure it.

---

<!-- Source URL: https://droip.com/docs/background/ -->

---

Background

The **Background** section in the **Style Panel** allows you to apply and customize background styles for any element.

You can layer multiple backgrounds, manage their order, set blend modes, and control how backgrounds interact with other elements’ content.

Accessing Background Settings
-----------------------------

![Background Options in Droip](https://droip.com/wp-content/uploads/2023/03/Background-type.webp)

To start customizing:

1. Select any element on the canvas.
2. Navigate to the **Style Panel**.
3. Expand the **Background** section.
4. Choose a background type and click the **+** icon to add it.

Each background is treated as a separate layer and can be edited, reordered, or removed individually.

Available Background Types
--------------------------

You can choose from the following background types:

* **Solid Color**
* **Linear Gradient**
* **Radial Gradient**
* **Conic Gradient**
* **Image**

Each type provides its own configuration panel with dedicated settings.

Solid Color Background
----------------------

![Solid Color Background in Droip](https://droip.com/wp-content/uploads/2023/03/Solid-Color-Background.webp)

**Solid Color** applies a single color as the background.

### How to Apply:

1. Select your element.
2. In the **Background** section, choose **Solid Color** from the background options.
3. Or, click the **+** icon to add it.
4. A color picker will appear. Choose your desired color or manually input a HEX or RGB value.

Note: You can also adjust opacity for solid color using the alpha slider in the color picker.

Linear Gradient Background
--------------------------

![Linear Gradient Background in Droip](https://droip.com/wp-content/uploads/2023/03/Gradient-Linear.webp)

**Linear Gradients** create a transition between two or more colors along a straight line.

### How to Apply:

1. Choose **Linear Gradient** as the background type.
2. The **Gradient Settings** panel will open.

### Gradient Settings:

* **Add Color Stops**: Click along the gradient bar to add stops. Use the color picker to select individual colors.
* **Adjust Position**: Drag stops or enter precise percentage values.
* **Set Angle**: Define the gradient direction in degrees (e.g., 0° for top to bottom, 90° for left to right).
* **Opacity**: Control individual color stop transparency.

Radial Gradient Background
--------------------------

![Radial Gradient Background in Droip](https://droip.com/wp-content/uploads/2023/03/Gradient-Radical.webp)

**Radial Gradients** transition colors outward from a central point, forming a circular or elliptical spread.

### How to Apply:

1. Choose **Radial Gradient** from the background type dropdown.
2. Configure your gradient in the **Gradient Settings** panel.

### Gradient Settings:

* **Color Stops**: Add, remove, or reorder as with linear gradients.
* **Position**: Set the center of the gradient.

Conic Gradient Background
-------------------------

![Conic Gradient Background in Droip](https://droip.com/wp-content/uploads/2023/03/Gradient-Conic.webp)

**Conic Gradients** rotate color transitions around a central point, creating a sweeping, circular effect.

### How to Apply:

1. Select **Conic Gradient** from the background type dropdown.
2. Customize using the **Gradient Settings**.

### Gradient Settings:

* **Color Stops**: Define the sequence of colors around the circle.
* **Start Angle**: Adjust where the gradient rotation begins (in degrees).
* **Center Point**: Specify the rotation origin.

This type is ideal for dynamic visuals like pie chart effects or artistic backgrounds.

Learn more about [Color Settings](https://droip.com/docs/color-settings/).

Image Background
----------------

![Image Background in Droip](https://droip.com/wp-content/uploads/2023/03/Image-type-background.webp)

The **Image** background lets you upload and configure images as element backgrounds.

### How to Apply:

1. Select **Image** as the background type.
2. Open **Background Image Settings** to configure it.

### Background Image Settings:

**Add Image**: Use the Media Manager to upload or select an image.

**Size**:

* **Auto**: Displays image at its original size.
* **Cover**: Scales the image to completely cover the element.
* **Contain**: Scales the image to fit inside the element without cropping.
* **Initial**: Uses the browser’s default setting.

**Attachment**:

* **Scroll**: The image scrolls with the page.
* **Fixed**: The image remains static as the page scrolls.

**Repeat**: Toggle repetition and choose direction: horizontal, vertical, or both.

**Position**: Precisely align the image using top/left/right/bottom or center positions.

Read detailed documentation on [Position settings](https://droip.com/docs/position/).

Managing Multiple Background Layers
-----------------------------------

![Managing Multiple Background Layers](https://droip.com/wp-content/uploads/2023/03/Background-Layer-Management.webp)

You can stack multiple background layers of different types for advanced designs.

### Available Layer Controls:

**Reorder**: To adjust the stacking order of multiple background layers, click and drag the (≡) icon next to each background. This allows you to move a layer up or down in the order, which changes how backgrounds are layered visually.

The topmost item in the list will appear above the others on the actual element.

**Toggle Visibility**: Click the **eye icon** to show/hide a background.

**Remove**: Click the **dash icon (-)** to delete a background layer.

Switching Background Types
--------------------------

![Switching Background Types in Droip](https://droip.com/wp-content/uploads/2023/03/Switching-background-style.webp)

You can change a background type without removing the existing layer.

1. Open the dropdown in the top-left corner of the layer’s header.
2. Select the new background type.
3. The settings panel will update accordingly.

Background Blend Mode
---------------------

![Background Blend Mode in Droip](https://droip.com/wp-content/uploads/2023/03/Background-Blend-Mode.webp)

Blend Modes define how a background layer interacts visually with layers below it.

### How to Apply:

1. Click the **drop icon** in the top-right of the background layer panel.
2. Choose a blend mode from the dropdown.

### Available Blend Modes

* Normal: Default value. The layer below does not bleed through the current layer.
* Multiply: The current layer and the layer below are multiplied, so this usually means a darkened effect.
* Screen: The current layer and the layer below are both inverted, multiplied, and inverted once again.
* Overlay: The current layer and the layer below are mixed together to show their lightness or darkness.
* Darken: If the current layer is darker than the layer below then the current layer is replaced, else no changes are applied.
* Lighten: If the current layer is lighter than the layer below then the current layer is replaced, else no changes are applied.
* Color Dodge: The layer below is divided by the inverse of the current layer.
* Color Burn: The layer below is inverted, divided by the current layer, and then inverted once more.
* Hard Light: ​​If the current layer is lighter than the layer below then the effect applied is Multiply else it is Screen.
* Soft Light: Similar to Hard Light but with a more diffused spotlight effect.
* Difference: Subtraction of the darkest color of the current layer and the layer below from the lightest one. The result is a high contrast effect.
* Exclusion: Similar to Difference but with lower contrast.
* Hue: The current layer’s hue is combined with the luminosity and saturation of the layer below.
* Saturation: Mixes hue and luminosity of the current layer and layer below while keeping saturation of the current layer.
* Color: Keeps the current layer’s hue and saturation and the layer below’s luminosity.

Each mode applies a different compositing method, often used to achieve visual effects or subtle overlays.

Clip Background
---------------

Use the Clip Background feature to define whether the backgrounds will extend underneath its padding, content, border, or text.

* **Padding:** Select this option to ensure the background extends up to the outer edge of the padding. (No background beneath the outer edge).
* **Content:** Choose the Content option if you want the background to be clipped to the content box.
* **Border:** Use this option to extend the background to the outer edge of the border. Note that the background will appear underneath the border but it’ll only be visible if the border has transparent sections or partially opaque sections (because of border style).
* **Text:** Select the text option to clip the background to the text element i.e. paint the background within the text.

Clip Images to Text
-------------------

Droip provides a convenient way to clip images to text for contemporary design trends. To achieve this, follow these steps:

1. Select your Text or Heading element.
2. Go to `Style` > `Backgrounds` and choose **Image** type background.
3. From the Image Background Settings, add your Background Image.
4. Open the `Clip Background` dropdown and select the `Text` option.
5. Go back to the image background settings to configure its placement.

And voila, you’ve successfully clipped your image back

---

<!-- Source URL: https://droip.com/docs/variables/ -->

---

Variables

The **Variables** feature in Droip allows users to define brand and global styles in one central location, simplifying the process of maintaining consistency across designs.

You can define variables for colors, font families, and sizes. These variables can then be applied seamlessly throughout the editor, ensuring effortless styling across different projects or sections of a website. When you update a variable value, that change is updated everywhere it’s used on your site.

There are several types of variables in Droip:

* Color variables
* Size variables
* Font variables

### **Color variables**

You can set color variables for:

* Text colors
* Background colors
* Border and text stroke colors
* Gradient color stops

### **Size variables**

You can set size variables for:

* Layout — grid width, height, min, max
* Size — height and width dimensions (including min and max)
* Typography — font size

### **Font variables**

* Font family

Any custom fonts (including Google fonts) uploaded to your site or Workspace are available when choosing a font family variable.

Accessing the Variables Panel
-----------------------------

![Accessing the Variables Panel in Droip](https://droip.com/wp-content/uploads/2025/02/Accessing-the-Variables-Panel.webp)

To open the **Variables** panel, click the `Variables` icon on the left sidebar.

### **Creating a Variable**

![Creating a Variable in Droip](https://droip.com/wp-content/uploads/2025/02/Creating-a-variable.webp)

1. Click the `+ Create Variable` button.
2. Choose the property you want to create a variable for, such as:
   * **Color**
   * **Font Family**
   * **Size**
3. Assign values to the selected property.

If you want to group multiple properties (e.g., color, size, and font) together:

![Creating a Variable Group](https://droip.com/wp-content/uploads/2025/02/Creating-a-Variable-Group.webp)

1. Click `+ Create Variable` at the bottom of the Variables panel and select the variable type.
2. Assign values to each property within the group.
3. Enter a **group name** for your variables.
4. Click **Save**, and you’re done!

#### **Example: “Primary” Group**

* **Color**: #000000
* **Font Family**: Arial
* **Font Size**: 12px

Assigning Modes to Variables
----------------------------

Droip’s Variables feature allows mode-based customization, where you can define **specific values for different modes** (e.g., light mode, dark mode, theme variants, etc.). Modes are fully customizable and adapt to your needs.

#### **Steps to Assign Modes:**

1. In the Variables panel, you’ll see columns for modes. Click on the `+Add` button to add as many modes as you need. Each Mode will appear in a separate column, for example: if you’ve named your modes “Dark Mode” and “Light Mode,” they will appear as separate columns.
2. Define property values for each mode:
   * Example:
     + For **Dark Mode**, set the color to #C12B2B.
     + For **Light Mode**, set the color to #5D4949.

You can create multiple modes depending on your design requirements and seamlessly toggle between them in the editor.

Managing Variables
------------------

![Managing Variables in Droip](https://droip.com/wp-content/uploads/2025/02/Managing-Variables.webp)

#### **Edit or Delete Properties**

* To edit an existing property, click the value to rename it or use the three-dot icon to copy CSS or delete the variable.

Applying Variables in Your Design
---------------------------------

![Applying Variables in Your Design](https://droip.com/wp-content/uploads/2025/02/Applying-Variables-in-Your-Design.webp)

Once variables are created, you can apply them to elements in your design:

1. Select an element in the editor.
2. In the styling panel, look for options like color, font, or size.
3. Choose the desired variable or group from the dropdown list.

The element will automatically inherit the properties defined in the variable, ensuring consistent styling.

Applying Variable Modes
-----------------------

There are many contexts in which variable modes can be used like creating accessible color themes, like high contrast mode or different themes for color blindness, using color variables.

Once modes are configured, you can apply them in your design workflow:

### Sections and Containers

![](https://droip.com/wp-content/uploads/2025/02/Sections-and-Containers-1024x613.webp)

Select the section/div/container in the editor. In the inline editor, locate the **Variable icon to open the Modes dropdown**. Choose the mode you want (e.g., Light Mode or Dark Mode). The entire section or container will inherit the properties of the selected mode.

### Page-Wide Application

![Page-Wide Application of Variables Modes](https://droip.com/wp-content/uploads/2025/02/Page-Wide-Application.webp)

To apply a mode to the entire page, click the `Page` option in the editor and select the mode from the dropdown menu.

📝 **Note**: For page-wide applications, if a variable mode has already been set for a section, you must change it to `inherit` for the page-wide variable mode to take effect.

Unlinking Variables
-------------------

![Unlinking Variables in Droip](https://droip.com/wp-content/uploads/2025/02/Unlinking-Variables.webp)

Whenever a variable is applied to a style, you’ll see an `unlink` icon next to it. Follow these steps to unlink a variable:

Click on the element that has a variable assigned (e.g., text, button, background).

In the **right sidebar**, navigate to the style section where the variable is applied (e.g., Typography, Color, Background). Look for the **unlink** icon next to the variable.

Click the `unlink` icon to remove the variable binding. The property will now be independent, allowing manual adjustments.

---

<!-- Source URL: https://droip.com/docs/license-key/ -->

---

License Key

A license key is a unique string of numbers and characters that verify authorized WordPress plugins and theme access.

To use Droip and get all the benefits of the premium plugin in your future endeavors, you need to activate the license of the Droip plugin. Please note that license activation is required to:

1. **Future Updates, Security Patches, and Bug Fixes**: Stay up-to-date with the latest features, enhancements, and security measures.
2. **Compatibility with the Latest WordPress Update**: Ensure seamless integration and optimal performance with the newest WordPress versions.

After purchasing a plan and installing the Droip Pro plugin, you’ll be prompted to **add and activate your license key** within the Droip WP dashboard.

📝 **Note**: Activating your Droip License Key is crucial for receiving automatic updates.

![Add license key in Droip](https://droip.com/wp-content/uploads/2023/02/License-Key.webp)

Access & Add Your License Key
-----------------------------

To access your license key, follow these steps:

1. Go to the Droip website and sign in using the email address used for the plan purchase.
2. Navigate to Account > `Subscriptions`.
3. Click on `Add Website` and input your domain name to generate a license.
4. `Copy` the license key from the dashboard.
5. In the WordPress admin dashboard, go to `Droip` > `Settings > License` and activate your license by pasting the copied key.

By activating your Droip License Key, you can benefit from regular updates and guarantee optimal performance.

For any further assistance or inquiries, feel free to contact our support team at **[[email protected]](/cdn-cgi/l/email-protection)**.

---

<!-- Source URL: https://droip.com/docs/paragraph/ -->

---

Paragraph

A **Paragraph** is an essential element that allows you to add blocks of text to any page. Using this element, text can be easily grouped with other related content like images, forms, etc.

How to Add Paragraphs
---------------------

![How to Add Paragraphs in Droip](https://droip.com/wp-content/uploads/2023/02/How-to-Add-Paragraph.webp)

To add a Paragraph:

1. Click on the `Insert` > `Elements` tab on the left side bar.
2. Scroll to the `Basic` section and drag the `Paragraph` element onto your canvas.

Paragraph Inline Editor
-----------------------

![Paragraph Inline Editor](https://droip.com/wp-content/uploads/2023/02/Paragraph-inline-editor.webp)

The Paragraph element offers an Inline Editor that allows you to adjust certain format settings. Simply select the element, and you’ll find the following options:

* **Text Color**: Choose the color of your text using the Color Picker to match your page’s theme and aesthetics.
* **Bold**: Apply bold formatting to emphasize important text.
* **Italics**: Italicize your text for emphasis or visual variety.
* **Link**: Open Link Settings to easily add hyperlinks to your text, connecting it to other sections or external resources.
* **AI Text Generator**: Generate text content using AI to save time and ensure consistent, coherent content across your webpage.
* **Dynamic Content**: Set up dynamic content for your paragraph, enabling real-time updates and personalized user experiences.

### Link Settings

![Link Settings in Paragraph](https://droip.com/wp-content/uploads/2023/02/Link-Settings.webp)

In the Link Settings, you can choose various link types from the drop-down list, including:

* **Web Address**: Link to external web pages, blog posts, or resources.
* **Email**: Link an Email address with a specific subject to facilitate easy communication.
* **Phone Number**: Link a Phone Number with country and area code for mobile users to initiate calls.
* **Page**: Link to other pages within your website to improve navigation and user flow.
* **Section**: Link to specific sections on the same page, enhancing user convenience.
* **Pop-up**: Link to pop-up for displaying additional content or capturing user input.

Additionally, you can set the **Rel** attribute, defining the relationship between the link and the current webpage. This helps improve accessibility, navigation, and SEO.

The following options are available for the Rel attribute:

* **Alternate:** Alternate representation of the current webpage such as a version for a different device, language, or format.
* **Author:** Link to the current web page’s author bio or contact information.
* **Bookmark:** Defines a relationship between the current document and a bookmark within the document.
* **External:** Referenced webpage is not on the same site as the current webpage.
* **Help:** Link to a resource with further help about the parent of the element and its descendants.
* **License:** Attests that the focal content of the current webpage is covered by the copyright license described by the referred webpage.
* **Next:** Current webpage is part of a series and the linked webpage is next in the sequence.
* **Nofollow:** Current webpage’s author does not endorse the linked webpage and this keyword tells the search engines to ignore the link relationship.
* **Noopener:** Attribute that tells the browser to navigate to the referred resource without giving browsing context access to the webpage that opened it. Comes in handy when opening unreliable links to prevent any tampering with the initial webpage.
* **Noreferrer:** Stops the browser from sending the current webpage’s address or other information when navigating to a different page.
* **Prev:** Current webpage is part of a series and the linked webpage is previous in the sequence.
* **Search:** Links to an interface using which the current web page and related pages can be searched.
* **Tag:** Link refers to a document describing a tag that is associated with the current webpage.

### Paragraph Options

![Paragraph options in Droip](https://droip.com/wp-content/uploads/2023/02/Paragraph-Options.webp)

Clicking on the `three-dot` icon at the end of the inline editor will open the Paragraph Options, providing further customization features:

* **Decorations**: Apply text emphasis such as Bold, Italics, or Underlined to enhance readability and highlight important information.
* **Letter**: Adjust Letter Case as Uppercase, Lowercase, or Capitalize for consistent styling and visual appeal.
* **Alignment**: Align text to the Left, Center, or Right to maintain a clean and organized layout.

How to Style Paragraphs
-----------------------

Paragraphs can be styled with the help of the tools available under the **Style Panel** located at the right sidebar. From here, you can adjust Typography, Structure, Size, and More. Please take a look at the [Style Panel Overview](https://droip.com/docs/style-panel-overview/) to know more.

AI-Generated Content
--------------------

![AI-Generated paragraph](https://droip.com/wp-content/uploads/2023/02/Ai-Generated-Content.webp)

For all text type elements including Paragraph, Droip gives you the option to automatically generate text content with the help of an AI.

This will not only save time but also ensures consistency and coherence in webpage content, allowing for greater focus on design.

Learn more about [AI Generator](https://droip.com/docs/ai-generator/).

---

<!-- Source URL: https://droip.com/docs/symbols/ -->

---

Symbols

**Symbols** in Droip let you turn any element, along with its child elements, into a reusable component.

Perfect for repeating sections like headers, footers, or CTAs, Symbols help maintain consistency across your site while simplifying updates. Edit once, and the changes reflect everywhere.

Creating a Symbol
-----------------

There are a few easy ways to create a Symbol in Droip:

* `Right-click` on any section or component and select `Create Symbol`.

![Creating a Symbol in Droip](https://droip.com/wp-content/uploads/2023/02/Creating-a-Symbol.webp)

* Or,`Select the component`, then click the `horizontal three-dot menu (⋯)` at the top of the right panel, and choose `Create Symbol`.

![Creating a Symbol from the Right panel](https://droip.com/wp-content/uploads/2023/02/creating-a-symbol-from-right-panel.webp)

* Or, From the `Layers panel`, right-click the section or component and select `Create Symbol`.

![Creating a Symbol from the Layers panel](https://droip.com/wp-content/uploads/2023/02/Layers-panel-Symbol.webp)

Then:

1. **Name your Symbol**.
2. **Choose a folder** to organize it within the **Symbols panel**.

Your new Symbol will now appear in the Symbols panel, ready for reuse.

Managing Symbols
----------------

![Managing Symbols from the Left panel](https://droip.com/wp-content/uploads/2023/02/Managing-Symbol.webp)

In the **Symbols panel**, each Symbol includes a **horizontal three-dot menu**  beside its name. Click it to:

* Edit the Symbol
* Rename it
* Delete it
* Set it as a **global header** or **footer**

Editing a Symbol
----------------

To make changes to the core version of a Symbol:

1. Click `Edit` from the Symbol menu.
2. You’ll enter `main mode`, where edits apply globally.
3. All instances of the Symbol across your site will instantly update.

Reusing a Symbol
----------------

To reuse a Symbol, simply **drag it from the Symbols panel** into any section of your page.

That’s it—it stays synced with the original.

Customizing a Symbol Instance
-----------------------------

Need a unique version of a Symbol on a page? You have two options:

### 1. Detach from Symbol

![Detaching a Symbol](https://droip.com/wp-content/uploads/2023/02/Detach-from-Symbol.webp)

* `Right-click` the Symbol on your page.
* Select `Detach from Symbol`.

The instance becomes a standalone element, fully editable.

💡 **Note**: Itwill no longer be linked to the main Symbol or other instances.

### 2. Update content without affecting the parent symbol

* Double click on the symbol and customize the content of the symbol instances like text, color, and font as needed without affecting the parent symbol.

Final Thoughts
--------------

You can use Symbols in two powerful ways:

**Identical Content**

* Edit the main Symbol and automatically update every instance.

**Unique Content**

* Detach a Symbol to customize it individually including style and content but it will no longer be linked to the main Symbol or other instances.
* Double click on the symbol and customize only the content of the instances like text, color, and font as needed without affecting the parent symbol.

---

<!-- Source URL: https://droip.com/docs/ai-generator/ -->

---

AI Generator

With Droip, you have the exciting capability to automatically generate content using an AI Generator. This powerful tool allows you to generate text content for your web pages and even entire page designs in just a matter of seconds! Let’s dive into how you can implement these amazing features.

📝 **Note**: To use the AI Generator feature, you need to have ChatGPT API enabled from `WP Admin` > `API Integration`!

Learn how to integrate [ChatGPT with Droip](https://droip.com/docs/api-integrations/).

Text Content Generation
-----------------------

The following is a list of the elements that have the AI Generator option for text content:

* `Heading`
* `Paragraph`
* `Text` (in List Item, Button, etc)

To generate AI content for your text elements (`Heading`, `Paragraph`, etc.), follow these steps:

1. **Select the Element**: Choose the desired element on your webpage that you wish to generate content for.
2. **AI Generator Icon**: In the inline editor, locate and click on the `AI Generator` icon associated with the selected element.
3. **Enter Description**: A window will pop up, prompting you to provide a brief description of the content you want to generate.
4. **Define Word Limit**: For more control over the generated text’s length, specify a word limit.
5. **Regenerate**: Click the `Regenerate` button, and you’ll now see your AI-generated text.

Remember that the AI-generated text will vary depending on the keywords and description you provide, so ensure your input is appropriate for the best results.

Webpage Design Generation
-------------------------

As mentioned earlier, with Droip, you can also AI generate webpage design! This is a total game-changer for the web design field because you can now let an AI design your page instead of spending precious time designing it on your own!

To generate a design, follow these steps:

1. **Add a Section Element**: Start by adding a `Section` element to your canvas.
2. **AI Generator Panel**: Open the inline editor, find the `AI Generator` icon for the Section element, and click on it.
3. **Detailed Description**: In the AI Generator window, provide a detailed description of the page design you want to generate. The more information you provide, the better the results.
4. **Reference Website (Optional)**: To guide the AI’s style, you can include a reference website that exhibits the design you’re aiming for.
5. **Click “Regenerate”**: Click on `Regenerate`, and your AI-generated design will appear on the page!

Please keep in mind that the generated design will be in HTML format, and the blocks used will be connected to their corresponding Droip elements. This design will form the basic structure of the page, with basic style settings applied, such as typography and size.

Once you have the AI-generated design, you can further customize it to suit your needs by adding media, applying interactions, and more.

Implement these powerful AI capabilities in Droip to streamline your content generation and webpage design process, saving you time and effort!

---

<!-- Source URL: https://droip.com/docs/transition/ -->

---

Transition

Transition is another amazing tool that can be used hand-in-hand with features like Stroke, Effects, Transform, and more to help create highly interactive web pages.

Use Transitions to make any animation between different states of an element to be much smoother and more pleasing to the eye.

![Droip transition](https://droip.com/wp-content/uploads/2023/09/Transition.webp)

Add Transition
--------------

To add a transition, select an element on your canvas that you’ve animated. Then head over to the Transition menu from the Style Panel which you’ll find on the right-hand side of your screen.

### States

Then, start by selecting which State you want the Transition to start. Options are the three States None, Hover, and Focus. You can also select this from the [States Menu](https://droip.com/docs/class-manager/#:~:text=of%20an%20element.-,States%20Menu,-Changing%20how%20an) located under Class & Sub-class.

### Add New

![Add new transition](https://droip.com/wp-content/uploads/2023/09/Add-Transition.webp)

Next, click on the plus icon to add a new transition. A new window should pop up from where you can customize your Transition settings.

**Transition Type:** Click on the dropdown situated at the top-left corner to select which type of animation you’re adding the transition for. Options include the following:

* All Properties
* Opacity
* Margin
* Padding
* Border
* Transform
* Filter
* Flex
* Background Color
* Background Position
* Box Shadow
* Text Shadow
* Width
* Height
* Max Width
* Max Height
* Min Width
* Min Height
* Border Width
* Border Color
* Border Radius
* Font Color
* Font Size
* Line Height
* Letter Spacing
* Text Indent
* Word Spacing
* Top
* Right
* Bottom
* Left
* z-Index
* Margin Top
* Margin Right
* Margin Bottom
* Margin Left
* Padding Top
* Padding Right
* Padding Bottom
* Padding Left

**Duration:** Define how long this transition will take. Click on the unit dropdown to select a different unit. Options include milliseconds (ms) and seconds (s).

**Delay:** Use this option to set the duration by which the Transition should delay if desired. Just like Duration, you can choose between the units milliseconds (ms) and seconds (s).

**Timing Function:** Click on the dropdown list from here to select the style of your Transition progression. Below is a list of the options available:

* **None:** No Timing Function defined.
* **Linear:** Animation maintains even speed.
* **Ease:** Animation increases in velocity during the middle and slows down at the end.
* **Ease-In:** Starts slowly and then animation speed increases until it ends.
* **Ease-Out:** Starts quickly but slows down as the animation progresses.
* **Ease-In-Out:** Starts slowly, then speeds up, and finally slows down again at the end.
* **Initial:** Apply the default value of this property to the element.
* **Inherit:** Set the same value as the parent element for this property.
* **Custom:** Set this if you want to use the Timing Editor to define a custom Timing Function.

Once you’re done setting up your transition, simply click on the X icon at the top-right corner to close this window. Then, you can click on the plus icon again to add more Transitions to your element if necessary

Custom Timing Editor
--------------------

![Custom Timing Editor](https://droip.com/wp-content/uploads/2023/09/Custom-Timing-Editor.webp)

The Custom Timing Editor is a nifty tool that can be used to define a custom progression of your animation transition. To access the Custom Timing Editor, from the Style Panel on the right, go to **Transition > Add New > Custom Timing Editor**.

On the Timing Editor, on the left, you will find more predefined Timing Function styles. The Default tab shows all of the styles but you can also click on the other tabs to see the styles of each specific category. Categories include:

* Ease In
* Ease Out
* Ease Both
* Spring

After selecting any one of these options, you can watch its Preview on the right by clicking on the play button at the top. Then, to customize it to suit your needs, simply drag the two toggles attached to each end of the graph on the preview.

Using Size Transition For Image Expansion on Hover
--------------------------------------------------

In this section, we’re going to show you how you can make your images interactive using the features Size and Transition.

### Setting Up

Start by adding a Div to your canvas. Then, place an Image element inside it and go to the Media Manager to select the Media you want to add.

Next, select the Div again and go to **Size** settings from the Style Panel on the right. Here, set its **Width** as 400px while keeping the rest of the settings the same.

### Expand on Hover

Now it’s time to take the steps needed to expand your image.

1. Select the Div and go to **Class & Sub-class > States Menu**. (Click on the expansion icon in its top-right corner if you don’t see it!)
2. Switch to the **Hover** state from the States Menu and go back to Size settings.
3. Here, change the Width to 1200px while once again keeping the rest the same.

### Use Transition to Polish in This Animation

Click on the Preview icon at the Topbar to view the current state of things. At this point, the animation should look disjointed as shown in the example below.

However, we can easily fix this using Transition by taking the following steps:

1. Select the Div and go to **Style Panel > Transition**.
2. Click on the plus icon to Add a new transition.
3. Here, set the Transition type as **Width**, Duration as **1000px**, and Timing Function as **Ease In**.

Now if you go back to check the Preview, then you’ll see the Image smoothly transitioning to its Hover state unlike before. In this case, we can say Transition is essentially what makes this animation work.

---

<!-- Source URL: https://droip.com/docs/settings/ -->

---

Settings

To make the most of your design and layout options in Droip, ensure you enable the following controls in the **Droip WordPress dashboard**:

![Droip General Settings](https://droip.com/wp-content/uploads/2025/02/droip-settings.webp)

Smooth Scroll
-------------

The **Smooth Scroll** feature enhances scrolling by adding a gradual transition effect. Users can toggle it on or off and adjust the smoothness level.

1. Go to Droip **WordPress Backend** > `Settings` > `General`.
2. Find `Smooth Scroll`.
3. Use the toggle switch:
   * **Enabled**: The page scrolls with a smooth transition effect.
   * **Disabled**: The page scrolls instantly without any easing.

### Adjusting Smoothness Level

When enabled, smoothness can be set between **1% (Instant)** and **100% (Smoothest)**:

* **1%**: No transition, abrupt movement.
* **50%**: Moderate smooth effect.
* **100%**: Most fluid scrolling.

To adjust, enter a value between **1% and 100%**. Changes apply instantly.

Image Optimization
------------------

Optimize uploaded images by converting JPG, PNG, and BMP files to `WebP format` for faster load times and improved performance.

Once enabled, uploaded images will be optimized without additional action.

SVG Upload
----------

By enabling the `SVG Upload` option, you can effortlessly upload SVG files and incorporate them into your designs.

JSON Files
----------

To leverage .json files in your projects, activate the `JSON Files` option. This allows uploading and management of .json files from your Media Manager.

Share View-Only Link
--------------------

![Share View-Only-Link in Droip](https://droip.com/wp-content/uploads/2025/02/Share-View-Only-Link.webp)

This feature allows you to generate a shareable, `view-only link` for the editor. It’s useful for sharing progress or drafts with clients without granting them editing access.

Use the Share View-Only Link to get feedback without risking changes to your project.

#### **How to Use:**

1. Navigate to `Settings`>`Advanced` in the Droip interface.
2. Locate the `Share View-Only Link` section.
3. Toggle the switch to enable this feature.
4. Click `Regenerate` to create a new preview link.
5. Use the `Copy` button to share the link with collaborators.

📝 **Note**: This feature is disabled for live production sites to maintain security and control over your project.

Export Data
-----------

![Export Project in Droip](https://droip.com/wp-content/uploads/2025/02/Export-Data-1.webp)

The Export Data feature enables you to save your current project setup, including pages, templates, styles, and other site information, for local backups or production deployment.

#### **What’s Included in the Export:**

* **Pages and Templates:** All the pages and templates used in your project.
* **View Ports and Fonts:** Settings related to responsive design and typography.
* **Styles and Variables:** Global CSS variables and design settings.
* **Content Manager:** Data related to dynamic content.
* **Assets and Site Info:** Uploaded assets and site metadata.

#### **How to Export:**

1. Navigate to `Settings` > `Advanced`.
2. Click the `Export` button under the Export Data section.
3. A progress modal will appear, showing the status of the export process.
4. Once completed, click `Download` to save the exported file to your device.

💡 **Tip**: Exported data is ideal for migrating your content between environments, such as from a staging server to production.

Import Data
-----------

![Import Project in Droip](https://droip.com/wp-content/uploads/2025/02/Import-Data.webp)

The Import Data feature lets you restore or migrate content by uploading previously exported Droip data files.

#### **How to Import:**

1. Navigate to `Settings` > `Advanced`.
2. Click the `Import` button under the Import Data section.
3. Select the exported file from your device.
4. The system will process the import, restoring the content and settings.

📝 **Note**: Only data exported from Droip is supported for import. Ensure the exported file is from a compatible Droip version.

---

<!-- Source URL: https://droip.com/docs/slider/ -->

---

Slider

The Slider component is basically a slideshow element that you can use to showcase any kind of content such as paragraphs, images, videos, buttons, and more!

Adding a Slider
---------------

![Adding a Slider in Droip](https://droip.com/wp-content/uploads/2023/03/How-to-Add-a-Slider.webp)

To integrate a Slider into your web page, follow these steps:

1. Go to the `Elements` panel.
2. Scroll down to the `Advanced` section and locate the `Slider` element.
3. Drag and drop the `Slider` element onto your canvas.

Slider Options
--------------

![Slider Options in Droip](https://droip.com/wp-content/uploads/2023/03/Sliders-Options.webp)

Customize your Slider using the Slider Options window accessible from the Slider’s Inline Editor. The available options are as follows:

1. **Add New** **Slide**: Click on `+ Add` next to Slides. The new item will appear at the bottom of the list.
2. **Reorder Slides**: Rearrange the order of Slides by simply dragging the slides.
3. **Set as Default:** Click the ellipsis icon next to a slide and select **Set as Default**. A circular check icon will indicate the default slide.
4. **Duplicate:** Quickly replicate a slide setup by choosing **Duplicate** from the ellipsis menu.
5. **Rename:** Rename slides for clarity by selecting **Rename** from the ellipsis menu, entering a new name, and clicking **Save**.
6. **Delete:** Remove a slide via the **Delete** option (disabled for the default slide).

### Adding Content to Slides

You can drag and drop any element into a slide and design it freely just like any other section in Droip. Build with text, images, buttons, or any component to match your layout needs.

Slide Navigation
----------------

From the **Slide Navigation** window, you can customize a Slider’s Indicators and Navigation Arrows.

**Indicators** show how many slides are present and highlight the currently active one.

**Navigation Arrows** let users manually move between slides using left and right arrows displayed over the slider.

### Indicators

![Slider Indicators in Droip](https://droip.com/wp-content/uploads/2023/03/Indicators.webp)

**Style**: Choose from seven different Indicator styles or select “None” to remove the Indicator.

**Set Indicators Position**: Access the Indicator Position window by clicking on “Set Indicators Position.”

![Set Slider Indicators Position](https://droip.com/wp-content/uploads/2023/03/Style-2.webp)

* **Position Grid**: Select the desired Indicator position from a 3×3 grid.
* **Horizontal Offset**: Define the Indicator’s horizontal shift.
* **Vertical Offset**: Define the Indicator’s vertical shift.
* **Orientation**: Choose between Horizontal or Vertical orientation for the Indicators.

### Arrows

![Set Slider Navigation as Arrows](https://droip.com/wp-content/uploads/2023/03/Arrows.webp)

**Style:** On the Arrows tab, you will find five different Navigation Arrow styles to choose from. You can also click on the None option to remove the arrows entirely.

If you do remove them, you can enable **Swipe Gestures** from **Slider Settings > Slider Transitions** so that users can swipe Slides using touch instead. You can also enable **Autoplay** in this case as well.

**Hide at Each End:** Enable this option to hide the left arrow on the first slide and the right arrow on the last slide. This helps indicate the first and last slide and prevents slide looping.

Slide Transitions
-----------------

![Set Slide Transitions in Droip](https://droip.com/wp-content/uploads/2023/03/Slide-Transitions.webp)

Customize Slide Animation from the Slide Transitions window. Open this panel by clicking on the transition icon.

1. **Select Slide**: Choose the slide for which you want to customize the transition.
2. **Slide In**: Set the entry animation style for the slide.
3. **Slide Out**: Set the exit animation style for the slide.
4. **Ease**: Define the transition effect between slides.
5. **Duration**: Set the transition duration in milliseconds.
6. **Slides Infinite Loop**: Enable this toggle to allow continuous looping of slides.
7. **Swipe Gestures**: Enable this option to enable users to swipe through the slides on touch devices.
8. **Autoplay on Loading**: Automatically change slides as soon as the page loads.

* **Delay**: Set the time interval before automatically transitioning to the next slide.
* **Stop Autoplay on Hover**: Enable this option to prevent slides from changing when hovered over.

How to Make Your Slider Work Like a Carousel
--------------------------------------------

By default, a Droip Slider shows one slide at a time. To display **multiple slides side-by-side**, like a carousel, follow the steps below.

### Create a Carousel Layout

![Create a Carousel Layout](https://droip.com/wp-content/uploads/2023/03/creating-a-carousel.webp)

From the **Layers panel**, select any **Slider item** inside your slider.

Then adjust the width to show multiple slides, to do that go to the **Style Panel** → **Sizin**g. Change the **Width** from 100% to:

* 50% to show 2 slides at once
* 33.33% to show 3 slides at once
* 25% to show 4 slides at once

Or set your **preferred width** depending on how many items you want visible at once.

Once configured, your slider will now act like a **carousel**, showing multiple items side-by-side that can scroll or auto-slide depending on your interaction settings.

---

<!-- Source URL: https://droip.com/docs/collection-references/ -->

---

Collection References

Droip’s Content Manager supports scalable, relationship-driven architecture using Reference and Multi-Reference fields. These fields allow you to create relational data models, making content reusable, consistent, and dynamic across your website.

What Is a Reference?
--------------------

A Reference field creates a one-to-one relationship between two content collections.

Think of it as a “foreign key” where one item points to another, rather than storing duplicated data.

What Is a Multi-Reference?
--------------------------

A Multi-Reference field forms a one-to-many relationship, where one item can link to multiple items in another collection.

This enables advanced relational setups like tags, multi-instructors, etc.

Reference Field
---------------

A **Reference Field** lets you connect a single item from one collection to another. It’s perfect for one-to-one relationships — like assigning a Department to a Course, or a Contributor to a Project.

### Why Use It?

* Reuse data instead of typing it again and again.
* Keep your content consistent across the site.
* Update once, and it changes everywhere it’s used!

**Example:** Instead of typing the department’s name for every course manually, you can connect each course to a department from the Departmentscollection.

### How to Add a Reference Field

Let’s say you already have a **Courses** collection, and you want to reference a Department from another collection called **Departments**.

* Go to the `collection` where you want to add the reference (e.g., Courses).
* Click `+ Custom Fields`, then choose `Reference.`

![Adding reference field in Droip](https://droip.com/wp-content/uploads/2025/04/Add-Reference-Field.webp)

* **Set the Target Collection:** Pick the `target collection` you want to reference (e.g., Departments)
* **Name the Field:** Give the `field` a name (e.g., Department)

![Choosing reference collection](https://droip.com/wp-content/uploads/2025/04/Choosing-Reference-.webp)

* Hit `Save` to apply the changes.

### Add Data to the Field

![](https://droip.com/wp-content/uploads/2025/04/Add-data-to-field.webp)

When you’re adding or editing a Course in your Courses collection:

* You’ll now see a dropdown for the reference field (e.g., Department)
* Choose one of the items from the Departmentscollection — that’s it!

### Displaying Reference Field on Your Website

Once you’ve connected data, you can display it on your page.

**On a List Page (e.g., all Courses)**

1. Add a `Collection Element` to the page.
2. Set the `Source` to Courses

![Displaying reference field on a list page](https://droip.com/wp-content/uploads/2025/04/Display-Reference-On-List-Page.webp)

3. Inside the Collection Element, add design elements (e.g., text).
4. For each element, click the `Dynamic Content icon` and set:

![Connect the reference field](https://droip.com/wp-content/uploads/2025/04/connect-reference-field.webp)

* **Type**: `Reference`
* **Name**: `Department`
* **Value**: What you want to display — like Post Title, etc.

**On a Template Page (e.g., single Course page)**

On a template page (e.g., dynamic page for each Course), the context of the current item is already known — so you don’t need a Collection Element for Reference Fields.

1. Drag a text/image or any design element anywhere on the page.
2. Click the `Dynamic Content icon`and set:

![Display reference field on a template page](https://droip.com/wp-content/uploads/2025/04/Display-Reference-On-a-Template-Page.webp)

* **Type**: `Reference`
* **Name**: `Department`
* **Value**: Choose what to show — like Name, Description,etc

Multi-Reference Field
---------------------

A **Multi-Reference Field** lets you link multiple items from another collection. This is ideal for one-to-many relationships — like assigning multiple Tags to a Course, or multiple Awards to a Project.

### Why Use It?

* Connects multiple items to a single entry.
* Easily manage grouped content (like tags, features, etc.)
* Keep related content dynamic and consistent
* Save time by reusing data across different items

**Example:** If you want to assign multiple tags to a course, instead of typing them all in manually, connect them from a Tags collection.

### How to Add a Multi-Reference Field

Let’s say you want to add multiple Tags to your a Course.

* Go to the collection where you want to add the multi-reference (e.g., Courses).
* Click `+ Custom Fields`, then choose `Multi-Reference`.

![Multi-reference field in Droip](https://droip.com/wp-content/uploads/2025/04/Multi-Reference-Field-1.webp)

* **Choose the Target Collection:** Pick the `target collection` you want to link. (e.g., Tags)
* **Name the Field:** Give the `field` a name. (e.g., Tags)

![Choose the multi-reference collection](https://droip.com/wp-content/uploads/2025/04/Choose-multi-reference-collection.webp)

* Click `Save` to finish.

### Add Data to the Field

![Add data to the reference field](https://droip.com/wp-content/uploads/2025/04/Add-Data-to-the-Field-1.webp)

When editing a Course:

* You can add **multiple items** from the Tags collection.

### Displaying Multi-Reference Data on Your Website

Since you’re referencing multiple items, this part is a little different from single references. You’ll need a collection element to display your multi-reference items.

**On a List Page (e.g., all Courses)**

1. Add a `Collection Element` andset the `Source` as `Courses`
2. Inside this element, add **another Collection Element.** This nested one will display the multi-referenced items.
3. Set the nested Collection Element:

![Displaying multi-reference on a list page](https://droip.com/wp-content/uploads/2025/04/Displaying-Multi-Reference-Data.webp)

* **Type**: Multi-Reference
* **Name**: Tags (or whatever your referenced collection is called)

4. Inside this nested collection element, add a text, image, or any design element. Click the `Dynamic Content icon`and set:

![Connect multi-reference field with the design](https://droip.com/wp-content/uploads/2025/04/Inside-Nested-element.webp)

* **Type**: `Post`
* **Value**: The field to display (e.g., Post Title)

**On a Template Page (e.g., a single Course page)**

1. Drag a `Collection Element` onto the page and set it as:

![Displaying multi-reference on a template page](https://droip.com/wp-content/uploads/2025/04/On-a-template-page-Drag-Collection-Element.webp)

* **Type**: `Multi-Reference`
* **Name**: Tags (or whatever your referenced collection is called)

2. Inside it, add elements to show each Tag.
3. Use the `Dynamic Content icon`and set:

![Connect multi-reference with the design on a template page](https://droip.com/wp-content/uploads/2025/04/Dynamic-Content-icon-1.webp)

* **Type**: `Post`
* **Value**: The field you want to show (e.g., Tag Name)

Updating Reference Content
--------------------------

Any changes you make in a referenced collection **automatically reflect** wherever that reference is used:

**Example**: Change a department’s info in Departments→ it updates across all courses referencing them.

This is especially powerful when managing large portfolios, product specs, or vendor info, etc.

Best Practices
--------------

✅ DO:

* Reference instead of duplicate — especially for **categories, tags, sponsors, clients, etc.**
* Name your fields clearly (e.g., Primary Author, Related Tags)
* Populate referenced collections first to avoid null dropdowns
* Use Multi-Reference when multiple associations are guaranteed or expected

🚫 AVOID:

* Over-nesting references (e.g., Contributor → Company → Country) unless necessary, it may complicate display
* Using Multi-Reference when a single reference is enough.

---

<!-- Source URL: https://droip.com/docs/accessibility/ -->

---

Accessibility

Accessibility ensures that websites and software tools are usable by a broader range of users, including those with disabilities. Droip’s **Accessibility** settings help improve the **UI experience** to ensure that the pages you design are flawless and user-friendly.

Accessibility Settings
----------------------

![Accessibility Feature in Droip](https://droip.com/wp-content/uploads/2023/02/Accessibility-1.webp)

The **Accessibility** settings are found on the right side of the **Topbar**, represented by the `Accessibility icon`. Clicking on it reveals the following options:

* **Large Text**: Increases text size for better readability, especially for users with visual impairments.
* **Disable Motion**: Turns off motion effects that might cause accessibility issues.
* **Big Black Cursor**: Replaces the default cursor with a larger, high-contrast black cursor.
* **Big White Cursor**: Replaces the default cursor with a larger, high-contrast white cursor.
* **Magnifier**: Adds a magnifying effect to the cursor, assisting users with low vision.
* **Increase Contrast**: Enhances overall color contrast to improve visibility.
* **Mouse Pointer Highlighter**: Highlights the mouse pointer, making it easier to locate on the screen.

Color Blindness Support
-----------------------

The **Color Blindness tool** allows users to adjust the display based on their specific **color vision deficiency**. Clicking on the dropdown provides the following options:

### Red-Green Color Deficiencies:

* **Protanopia**: Red-blindness (absence of red cones).
* **Protanomaly**: Red-weakness (some shades of red are visible).
* **Deuteranopia**: Green-blindness (absence of green cones).
* **Deuteranomaly**: Green-weakness (some shades of green are visible).

### Blue-Yellow Color Deficiencies:

* **Tritanopia**: Blue-blindness (absence of blue cones).
* **Tritanomaly**: Blue-weakness (some shades of blue are visible).

### Full-Color Deficiencies:

* **Achromatomaly**: Partial color blindness (cones function poorly, vision relies on rods that do not process color well).
* **Achromatopsia**: Total color blindness (only shades of gray are visible).

### Other Visual Impairments:

* **Cataracts**: Simulates blurred vision caused by clouding of the eye’s lens.

By prioritizing **accessibility**, Droip ensures an **inclusive and user-friendly environment**, allowing **all users** to interact with the platform seamlessly, regardless of their visual abilities.

---

<!-- Source URL: https://droip.com/docs/rich-text/ -->

---

Rich Text

Rich Text allows you to add text with various formatting options to your website, such as **bold**, *italic*, underline, different font styles, and more.

![](https://droip.com/wp-content/uploads/2023/03/Adding-Rich-Text.webp)

Adding Rich Text
----------------

To add rich text in Droip, follow these steps:

1. Go to the `Elements Panel` on the left sidebar.
2. Drag and drop the `Rich Text` element onto your page.
3. Type your text and use the formatting options to style it as desired.

Formatting Options
------------------

Droip’s Rich Text Editor provides the following formatting options:

* Bold
* Italic
* Underline
* Headings (H1 to H6)
* Lists (ordered and unordered)
* Links
* Images
* Code
* Blockquotes

Customizing Rich Text
---------------------

You can further customize the rich text by using the Style panel located at the right sidebar:

1. In the Style panel, you can change the font family, size, color, and more for different elements of the text.
2. You can also add custom CSS to change the appearance of the rich text.

Rich text is a powerful tool for adding text to your website and making it more engaging and readable. With the Rich Text element and the formatting and styling options in Droip, you can easily create rich and well-formatted text for your website.

---

<!-- Source URL: https://droip.com/docs/effects/ -->

---

Effects

Elevate your elements’ visual impact by applying effects like altering Brightness, Opacity, Hue, and more from the **Style Panel** > **Effects**.

![Effects of Droip](https://droip.com/wp-content/uploads/2023/09/Effects.webp)

Applying Effects
----------------

You can apply effects either directly on the element or on the backdrop behind it. Here’s how:

* **On Element:** Apply effects directly to the element and its children.
* **On Backdrop:** Apply effects to the backdrop behind the element.

Available Effects
-----------------

Explore various effects and their settings:

* **Opacity:** Adjust element transparency using the Opacity property.
* **Blur:** Apply a blurred effect to your element.
* **Brightness:** Control the brightness level of your element.
* **Contrast:** Fine-tune your element’s contrast.
* **Saturation:** Define the vibrancy of your element’s colors.
* **Invert Color:** Invert the colors of the element.
* **Grayscale:** Transform the element into grayscale.
* **Hue Rotate:** Change the color hue of the element.
* **Sepia:** Add a sepia-toned effect for a vintage look.

On Element vs On Backdrop
-------------------------

As you may have noticed, Effects can be applied to an element or to the backdrop. Selecting **On Element** means only the element and its children are affected by the changes.

On the other hand, selecting **On Backdrop** means that only the backdrop behind the element will be affected. Check out the images below to get a better idea.

![Blur effect On Element](https://droip.com/wp-content/uploads/2023/09/On-Element-vs-On-Backdrop.webp)

Blur filter effect ‘On Element’ for Heading

![Blur effect on backdrop](https://droip.com/wp-content/uploads/2023/09/Effects-1.webp)

Blur filter effect ‘On Backdrop’ for Heading

In the above images, the first instance is the effect of the blur filter on the Heading element. This adds a blurry effect to the entire text box up to its margins.

On the other hand, the second instance shows the effect of the blur filter on the backdrop of the Heading element. This causes the portion of the backdrop occupied by the Heading element to blur but the text remains sharp.

💡 **Tip**: Keep in mind that, for the backdrop to be visible, at times you might have to lower the opacity of your element. Of course, this is only in case of elements that are totally opaque or have an opaque background.

Cursor
------

From the dropdown at the very top, you can change the style of the Cursor for an element. This feature helps improve interactivity since users associate certain pointers with specific types of elements.

For instance, the ![](https://lh4.googleusercontent.com/clhANLKpowYEZfl9Balar3rv_8tIps0d2afdXx9NhV4uEISSE7qZk0wz2grqxQipbiW4d0cApQ6DSGKV7Z7yiPJU0-hiIeplBkOWqibaRz_OmWdtuXmhxQRCAkq1cQDctHGhaNzQDUpxGHN4ywsxwxw) (Text) Cursor is associated with blocks of text while the ![](https://lh4.googleusercontent.com/o9qXEb1hBZ8lDAEXufT3nP9jomKkud-babTDw7QVmTEwMETivlKuKFot5wnlFwWwkUIRbKMomCJQRM5DBn3fcQPv0fDDO0wz87zziCspbvfW-qIcGHFNGl8Tc9CYEx2Sn6gPyXQPXBy0t3UC3X8qGLM) (Grab) Cursor lets the user know that the element can be dragged.

Now let us go over the various Cursor styles and when they can be used.

![Droip cursor style](https://droip.com/wp-content/uploads/2023/09/Droip-cursor-style.webp)

* **Default:** Classic Arrow Cursor.
* **Auto:** Cursor style changes automatically based on browser settings.
* **None:** Invisible cursor (use sparingly).
* **Context Menu:** Cursor for right-click context menus.
* **Help:** Cursor indicating help availability.
* **Pointer:** Cursor for links or buttons.
* **Progress:** Cursor for indicating webpage loading.
* **Wait:** Cursor for busy websites.
* **Cell:** Cursor for selecting tabular cells.
* **Crosshair:** Cursor for indicating selection or charts.
* **Text:** Cursor for horizontal text input.
* **Vertical Text:** Cursor for vertical text input.
* **Alias:** Cursor indicating alias creation.
* **Copy:** Cursor for copying.
* **Move:** Cursor indicating element movement.
* **Not Allowed:** Cursor for blocked actions.
* **Grab:** Cursor for draggable elements.
* **Grabbed:** Cursor indicating a grabbed element (best for Focus state).
* **Col Resize:** Cursor to show that a column can be resized by dragging horizontally.
* **Row Resize:** Cursor to show that a row can be resized by dragging vertically.
* **N Resize:** Cursor used to indicate that an element’s edge is to be moved up (north).
* **E Resize:** Cursor used to indicate that an element’s edge is to be moved right (east).
* **S Resize:** Cursor used to indicate that an element’s edge is to be moved down (south).
* **W Resize:** Cursor used to indicate that an element’s edge is to be moved left (west).
* **NE Resize:** Cursor used to indicate that an element’s edges are to be moved up and right (northeast).
* **NW Resize:** Cursor used to indicate that an element’s edges are to be moved up and left (northwest).
* **SE Resize:** Cursor used to indicate that an element’s edges are to be moved down and right (southeast).
* **SW Resize:** Cursor used to indicate that an element’s edges are to be moved down and left (southwest).
* **EW Resize:** Cursor used to indicate that an element’s edges are to be moved right and left (northeast). In short, signifies a bidirectional resize.
* **NS Resize:** Cursor used to indicate that an element’s edges are to be moved up and down (north-south). In short, signifies a bidirectional resize.
* **NESW Resize:** Cursor that points to north-east-south-west and that signifies a bidirectional resize.
* **NWSE Resize:** Cursor that points to north-west-south-east and signifies a bidirectional resize.
* **Zoom In:** Use this to show that an element/page can be zoomed in.
* **Zoom Out:** Use this to show that an element/page can be zoomed out.

---

<!-- Source URL: https://droip.com/docs/filter-wordpress-posts/ -->

---

Filter WordPress Posts Using Collection

In Droip, you can create a dynamic filtering functionality for WordPress posts using the Collection element.

This feature allows users to filter WordPress posts based on categories, tags, and any custom taxonomy you have on your WordPress Site

### Step 1: Create a Collection for WordPress Posts

![Step 1: Create a Collection for WordPress Posts](https://droip.com/wp-content/uploads/2024/09/Create-a-collection-for-wordpress-posts-1.webp)

1. **Add a Collection Element:** Begin by adding a `Collection Element` to your Droip page. Connect this Collection Element to your WordPress posts. This is where your WordPress post data will be displayed dynamically.
2. **Set Collection Type:** In the Collection settings, set the `Collection Type` to `Post`. For the `Post` field, select `Posts`. This will ensure that your Collection is pulling data from your WordPress posts.
3. **Configure the Collection Settings:** Name your collection appropriately in the `Layers`, i.e Post Collection.
4. **Design the Collection List:** Use Droip’s element and styling tools to customize the appearance of the posts as per your design needs. You can use **dynamic elements** like post title, featured image, excerpt, and metadata (date, author, etc.).

### Step 2: Create a Collection for Filter Functionality

![Step 2: Create a Collection for Filter Functionality](https://droip.com/wp-content/uploads/2024/09/create-a-collection-for-filter-funtionality-1.webp)

Next, we will create another Collection that will act as the filter for our posts.

1. **Add a New Collection Element:** This collection will be responsible for creating the filter functionality. The key to this Collection Element is that it should only contain the **checkbox element** as collection items.
2. **Add Checkbox:** Insert the `Checkbox Element` into this Collection to dynamically display the categories, tags, or custom taxonomies as checkboxes that your posts fall under.

### Step 3: Configure Collection Settings for the Filter

![Step 3: Configure Collection Settings for the Filter](https://droip.com/wp-content/uploads/2024/09/configure-collection-settings-for-the-filter-1.webp)

Now, configure the Collection settings for the filter functionality to connect it with your post collection.

1. **Set Collection Type:** In the Collection settings, set the `Collection Type` to `Terms`. For the `Post` field, select `Posts`.
2. **Select the Appropriate Taxonomy:** In the `Taxonomy` field, select the relevant taxonomy you want to filter by. This could be `Categories`, `Tags`, or any custom taxonomy you have on your WordPress site.
3. **Set Relation as Filter:** Under the `Relation` option, tick the checkbox to enable `Filter`. This will link the checkbox collection with the filtering functionality.
4. **Link the Filter Collection with the Post Collection:** In the `Collection` field, select the Collection you want to apply the filter functionality on. This step connects the checkboxes to your list of posts, allowing them to filter the posts based on the selected criteria (categories, tags, etc.).

### Step 4: Preview the Filter Functionality

![Step 4: Preview the Filter Functionality](https://droip.com/wp-content/uploads/2024/09/preview-the-filter-functionality-1.webp)

Once the settings are configured, preview your page to see the filter in action.

Users should now be able to check and uncheck the checkboxes, and the WordPress posts will dynamically update based on the selected filters.

With Droip’s Collection Element, creating a filter functionality for WordPress posts is a simple yet powerful feature. By using dynamic data, and advanced collection settings, you can offer a seamless and interactive user experience, allowing visitors to filter posts by categories, tags, or other taxonomies.

---

<!-- Source URL: https://droip.com/docs/topbar-overview/ -->

---

Topbar Overview

The Topbar in Droip provides a range of powerful tools to streamline your website-building process. Let’s explore each element of the Topbar:

![Topbar in Droip](https://droip.com/wp-content/uploads/2023/02/Topbar.webp)

Topbar Menu
-----------

Starting from the left side of the Topbar, you will find the `Topbar Menu`. Click on the dropdown button beside Droip’s logo to access the following options:

![Topbar Menu in Droip](https://droip.com/wp-content/uploads/2023/02/Topbar-Menu.webp)

### **View Options**

![Canvas View Options in Droip](https://droip.com/wp-content/uploads/2023/02/Canvas-View-Options.webp)

Hover over `View Options` to access the menu settings. From here, you can choose which menus to keep visible in the editor while working on your website.

### **Font Library**

![Font Library in Droip](https://droip.com/wp-content/uploads/2023/02/Upload-Custom-Fonts-1024x616.webp)

Clicking on `Font Library` opens a new window with three tabs:

* **Google Fonts**: Browse and select from a collection of free web fonts provided by Google.
* **Installed Fonts**: View the fonts already installed in your Droip project.
* **Custom Fonts**: Upload and use your own fonts on your website. Learn how to [upload custom fonts](https://droip.com/docs/upload-custom-fonts/).

### **Show Onboarding**

Click `Show Onboarding` to start a guided tour of the website builder. This will give you an overview of all features and where to find them.

### **Shortcuts**

Access a comprehensive list of keyboard shortcuts to speed up your design process. Read more about [Keyboard Shortcuts](https://droip.com/docs/keyboard-shortcuts/).

### **Back to Admin**

Click `Back to Admin` to return to the WordPress Admin Dashboard.

**Breakpoints**
---------------

![Breakpoints in Droip](https://droip.com/wp-content/uploads/2023/02/Breakpoints-1.webp)

At the center of the Topbar, you’ll find four different device icons. These are known as `Breakpoints`, allowing you to control webpage responsiveness across different screen sizes. By default, the Topbar includes:

* **Desktop**
* **Tablet**
* **Mobile Landscape**
* **Mobile**

Additionally, you can set unlimited **Custom Breakpoints** according to your needs. Learn more about [Breakpoints](https://droip.com/docs/breakpoints/).

**Global Search**
-----------------

![Global Search in Droip](https://droip.com/wp-content/uploads/2023/02/Global-Search-1.webp)

Click the `Magnifying Glass` icon or press `CMD + ?` to access **Global Search**. From here, you can search for **Elements, Pages, and On-page Elements** quickly and efficiently.

**Canvas Control**
------------------

![Canvas Control in Droip](https://droip.com/wp-content/uploads/2023/02/Canvas-Control.webp)

The `Canvas Control` feature allows you to customize the display and behavior of the canvas while designing. It is represented by the `Scale Percentage` dropdown on the Topbar.

With Canvas Control, you can:

* Adjust the **scale** of the canvas.
* Show or hide **rulers** to align elements precisely.
* Display or hide **guides** for a structured layout.

Learn more about [Canvas Control](https://droip.com/docs/canvas-control/).

**Audit**
---------

![Audit Feature in Droip](https://droip.com/wp-content/uploads/2023/02/Audit.webp)

The `Audit` feature, represented by the **Triangle Exclamation icon**, performs automatic accessibility checks on the following aspects:

* **Alt Text Missing** (for images)
* **Link Missing** (for necessary elements)
* **Class Name Missing** (for proper structuring)

Learn more about [Page Audit](https://droip.com/docs/page-audit/).

**Accessibility**
-----------------

![Accessibility in Droip](https://droip.com/wp-content/uploads/2023/02/Accessibility.webp)

Following the Audit feature, the `Accessibility` option allows users to customize the interface to suit their needs, particularly for those with disabilities.

Learn more about [Accessibility](https://droip.com/docs/accessibility/) in Droip.

**Preview**
-----------

Click on the `Play` icon to view a **full preview** of your designed webpage, allowing you to see how it will appear to visitors.

**Auto Save**
-------------

Droip features a seamless `Auto Save` mechanism to ensure continuous saving of your work. This prevents data loss, even if you forget to manually save.

The **Status Label** at the top-right corner indicates saving progress. **“Saving”** appears when changes are in progress. **“Auto Saved”** confirms the save is complete.

You can disable **Autosave** by clicking the dropdown arrow and unchecking **Enable Autosave**.

📝 **Note**: Droip automatically saves your page content within 3 seconds of user inactivity.

---

<!-- Source URL: https://droip.com/docs/figma-to-droip/ -->

---

Figma to Droip

The **Figma to Droip** plugin streamlines the workflow between design and development, empowering you to create stunning websites with unparalleled ease and efficiency.

* Seamless transfer of design components and styling from Figma to Droip.
* Access to Droip’s comprehensive set of features and tools for website development.
* Effortlessly maintain design consistency and efficiency throughout the design-to-development process.

[](https://droip.com/wp-content/uploads/2024/03/figma-to-droip-demo.mov)

Installation
------------

Getting started with Figma to Droip is simple:

1. Open `Figma` and navigate to the `Resources` tab.
2. Search for `Figma to Droip` and select the plugin.
3. Click on `Install`.

The Figma to Droip plugin will now be available in your Figma interface.

Using the Plugin
----------------

1. Prepare your Figma Design:

* Ensure your Figma design is complete and uses well-organized layers and groups.
* Utilize Figma’s auto layout feature to adjust every section for optimal transfer to Droip.

2. Copy your Design:

* Select the Figma frame or group containing your website design.
* Click on `Generate` on the Figma to Droip plugin.
* Once generated, simply choose `copy`.

3. Paste into Droip:

* Open Droip and navigate to your desired project or create a new one.
* Paste the copied Figma design element into the Droip workspace using `Cmd + V`.

4. Refine & Launch:

* Droip will import your Figma design, maintaining layouts, styles, and spacing.
* You can now further customize your website within Droip’s user-friendly interface.
* Add interactivity, personalize elements with content and media, and adjust functionalities as needed.
* Once satisfied, hit publish to showcase your live website to the world!

Guidelines
----------

For the following element types, use these specific built-in element names in Figma for easy identification during import.

For example, if you have a button, label it as “\_\_button\_\_”, “\_\_Button\_\_”, or “\_\_BUTTON\_\_”. By following this naming convention, Figma to Droip can better transfer the design and convert the elements accordingly.

|  |  |
| --- | --- |
| **Element Type** | **Element Name** |
| Button | Button, button, BUTTON |
| Form | Form, form, FORM |
| Input | Input, input, INPUT |
| Textarea | Textarea, textarea, TEXTAREA |
| Section | Section, section, SECTION |
| Container | Container, container, CONTAINER |

---

<!-- Source URL: https://droip.com/docs/content-manager-overview/ -->

---

Overview

The Content Manager is a powerful feature in Droip designed to streamline the creation, organization, and management of dynamic content on your website.

It serves as a central hub where you can define content structures, input data, and seamlessly integrate this data into your site’s design dynamically.

Whether you’re managing a blog, portfolio, client database, or any other type of content, the Content Manager provides a user-friendly interface to handle it all efficiently.

**Key Features and Benefits**

* **Centralized Content Management**: Manage all your content in one place, making updates and organization simple and efficient.
* **Dynamic Content Integration**: Easily integrate your content with your website’s design, ensuring that updates are reflected across all relevant pages automatically.
* **Custom Fields**: Utilize a variety of field types (text, images, videos, dates, etc.) to capture exactly the information you need.
* **Collection Presets**: Start quickly with predefined collections for common content types like portfolios, projects, and team members.
* **Scalability**: Effortlessly handle a growing amount of content without compromising on performance or usability.
* **Efficiency**: Save time with bulk actions, conditional visibility rules, and other features designed to enhance your workflow.

Accessing the Content Manager
-----------------------------

![Accessing the Content Manager](https://droip.com/wp-content/uploads/2024/08/Overview-1024x614.webp)

To access the Content Manager in Droip:

1. **Access the Droip editor**: Start by logging into the backend of your Droip website and open the Droip editor.
2. **Navigate to the Content Manager**: From the editor, find and click on the “Content Manager” option on the Topbar.

Content Manager Overview
------------------------

Static content describes content that must be manually updated. Whereas when you use dynamic content, your design is linked to Content Manager data so you can update multiple content instances all at once.

![Content Manager Overview](https://droip.com/wp-content/uploads/2024/08/explaining-dynamic-content-1024x613.webp)

### Step 1: Create Collections

To start, navigate to the Content Manager and click on Add New. Name your collection based on the type of content it will hold (e.g., “Blog Posts,” “Products,” “Team Members”).

If you prefer, you can start with a predefined collection template that matches your content type. This can save time and provide a ready-made structure for your content.

### Step 2: Define Collection Fields

Collection Fields define the structure of your Collection, dictating the type of information each item will hold. For instance, a “Blog Post” Collection might include fields for the title, author, publish date, and content.

1. **Add Fields**: When creating or editing a Collection, you can add various fields such as text, image, date, number, URL, etc. Each field type is designed to capture specific kinds of data, allowing for precise content management.
2. **Customize Fields**: Customize each field to suit your needs. For example, you can set a text field as mandatory, limit the number of characters, or allow rich text formatting.

### Step 3: Add Collection Items

Once your Collection is set up, you can start adding individual items. Each item in the Collection will have the fields you defined where you can input data for each field.

### Step 4: Display Dynamic Content

With your Collection items ready, you can now integrate them into your website using Droip’s elements:

* **Collection Lists**: The Collection element allows you to display lists of your Collection items on any page. For instance, you can create a dynamic blog feed on your homepage or showcase team members on an “About Us” page. Map the fields from your collection to the corresponding elements in your design (e.g., map the “Name” field to a text element, and the “Profile Picture” field to an image element).
* **Collection Pages**: Collection Pages enable you to design a single layout that applies to all items in a Collection. For example, if you have a “Team Members” Collection, you can design a page layout with placeholders for the team member’s name, picture, bio, and contact information. The data for each team member will automatically populate these placeholders when the page is viewed.

---

<!-- Source URL: https://droip.com/docs/comments/ -->

---

Comments

Droip lets you leave comments directly on the canvas, enabling real-time feedback and smoother collaboration between designers, developers, clients, and teams, all without ever leaving the editor.

Whether you’re reviewing a page, requesting changes, or explaining a design choice, Droip’s comment system keeps conversations contextual and actionable.

Overview
--------

The Comment feature allows users to:

* Leave comments anywhere on your layout on the canvas.
* Tag collaborators with @mentions
* Keep track of open, unread, and resolved comments
* Centralize all feedback into a single, organized panel

Think of it as collaborative feedback built right into your design workflow.

Permissions
-----------

Users with **Content-Only** access can leave comments directly on the canvas, but won’t see the full Comments panel.

Users with **Full Access** can view, reply to, and manage all comments.

Learn more about [access levels](https://droip.com/docs/role-manager/).

Where to Find Comments
----------------------

To open the Comment Panel, click the **Comment icon** (💬) on the top toolbar. This will enable the comment mode and open a side panel where you can:

* See all comments
* Search through feedback
* Filter by: **All**, **Unread**, or **Resolved**

💡 **Note**: Comments are tied to individual pages, so feedback stays focused and organized.

How to Add a Comment
--------------------

![How to Add a Comment in Droip](https://droip.com/wp-content/uploads/2025/08/how-to-add-a-comment.webp)

1. Enable comment mode using the `comment icon`.
2. Click anywhere on the page (not directly on the element, but on the layout).
3. A floating comment box will appear where you clicked.
4. Type your feedback.
5. Optionally `@mention` a teammate (if multi-user access is enabled)
6. Click the Upward Arrow icon to submit the comment

💡 **Note**: Comment markers are shown as floating pins on the canvas so collaborators know where the comment is anchored.

Collaborate With Your Team
--------------------------

![Collaborate With Your Team Through Comments](https://droip.com/wp-content/uploads/2025/08/collaborate-with-your-team.webp)

You can @mention collaborators inside a comment to direct feedback to them. All users with appropriate permissions can view, reply to, and resolve comments.

Managing Comments
-----------------

* Reply: Start a thread beneath any existing comment
* Resolve: Mark comments as completed or addressed
* Mark as Unread/Delete: Click on a comment on the canvas and click the More (…) menu

Best Practices
--------------

* Use clear and actionable language when leaving feedback  
  e.g., “Let’s increase the padding on this section by 20px for better spacing”
* Group comments by section or component to keep discussions organized
* Resolve comments once completed to maintain a clean workspace
* Use @mentions for accountability and faster collaboration
* Commenting on staging versions during page revisions

---

<!-- Source URL: https://droip.com/docs/api-integrations/ -->

---

API Integrations

Droip offers seamless API integrations to empower your website-building experience with advanced features and functionalities. Below are the details on how to integrate each API into your Droip projects:

![](https://droip.com/wp-content/uploads/2023/02/API-Integrations.webp)

Artificial Intelligence (AI) Integration
----------------------------------------

The **Artificial Intelligence (AI)** feature enables text & layout generation capabilities within Droip by integrating an external AI model. Droip currently supports **Phase-1 AI** for text generation with future phases we’ll introduce more advanced features. To integrate AI, follow these steps:

1. Log in to your OpenAI account at [platform.openai.com](https://platform.openai.com/).
2. Go to your `Dashboard` > `API Keys`.
3. Click `Create new secret key` to generate your API key.
4. Copy the key and store it securely—you’ll need it in the next step.
5. In your WordPress dashboard, go to `Droip` > `Settings` > `Integrations`.
6. Enable the `Artificial Intelligence (AI)` option from the integrations list.
7. Click the three-dot menu (⋯) next to the AI option and paste your ChatGPT API key.
8. Once saved, Droip will be connected with ChatGPT—enabling AI-powered features within the editor.

Unsplash API Integration
------------------------

The Unsplash API is a modern JSON API that grants access to an extensive collection of high-quality, free-to-use photos. To integrate Unsplash with Droip and easily add images to your projects, follow these steps:

1. Go to the [Unsplash API](https://unsplash.com/developers) website and sign in or create an account.
2. Navigate to the `API Keys` section and click on the `New Application` button.
3. Fill in the required details for your application, including the name, description, and website URL.
4. Once your application is created, you’ll receive your `Access Key` to use with the Unsplash API.
5. In the Droip WordPress dashboard, navigate to API Integrations and click on `Connect`. Enter your `Unsplash Access Key` to establish the connection between Unsplash and Droip.

Pexels API Integration
----------------------

The Pexels API offers a free JSON-based interface, providing access to high-quality, curated photos and videos from Pexels’ vast library of over 1 million assets. To integrate Pexels content into your Droip projects, follow these steps:

1. Go to the [Pexels API](https://www.pexels.com/api/) website and sign up for an API key.
2. You’ll receive your `API Key` after signing up.
3. In the Droip WordPress dashboard, navigate to API Integrations and click on `Connect`. Enter your `Pexels API Key` to enable seamless integration between Pexels and Droip.

ReCAPTCHA Integration
---------------------

ReCAPTCHA is a free Google service that protects websites from spam and abuse by verifying human users. To set up ReCAPTCHA integration with Droip, follow these steps:

1. Navigate to the [reCAPTCHA Admin Console](https://www.google.com/recaptcha/admin).
2. Sign in with your Google account to proceed.
3. Register a new site by providing a label for identification purposes.
4. Choose the type of reCAPTCHA you wish to use (v2 or v3).
5. Enter the domain names of your website where you want to use reCAPTCHA.
6. Set the owners’ email addresses who should have access to the reCAPTCHA report.
7. Tick the ‘Send alerts to owners’ checkbox to receive email alerts for any misconfigurations or suspicious traffic.
8. Submit the form to generate your Google reCAPTCHA Site Key and Secret Key.
9. Copy and securely store these keys.
10. In the Droip WordPress dashboard, navigate to API Integrations and click on `Connect` to integrate reCAPTCHA.
11. Select your `reCAPTCHA version` from the drop-down.
12. Enter the `Site Key` and `Secret Key` generated in the previous steps.

---

<!-- Source URL: https://droip.com/docs/form-elements/ -->

---

Form Elements

A web form is an HTML form that lets users enter their information. There’s no “one size fits all” when it comes to web forms.

Depending on your business needs and the type of user data you want to collect, you can craft any web forms that fit your needs with Droip.

How to Add a Form
-----------------

![Form Builder in Droip](https://droip.com/wp-content/uploads/2023/03/How-to-Add-a-Form.webp)

To add a Form to your page, follow these simple steps:

1. Open the `Insert` Panel from the right sidebar.
2. Navigate to `Elements` > `Forms`.
3. Drag and drop the Form element onto your canvas.

### Default Form Structure

The Form comes with a set of default form elements, including:

* Heading
* 4 input fields labeled as Name, Email, Subject, Description
* Submit Button

Available Form Elements
-----------------------

Droip offers various elements to help you design functional forms:

* **Label**: Describes a field’s purpose for users.
* **Input**: Captures single-line text (e.g., name, email, phone).
* **Textarea**: For multi-line input (e.g., comments, messages).
* **Selector**: Provides a dropdown list of options.
* **Checkbox**: Lets users select one or more options.
* **Radio Button**: Allows selection of only one option from a list.
* **Form Button**: Submits the form.
* **reCAPTCHA**: Protects against spam using Google’s service.
* **File Upload**: Enables users to attach files.

📝 **Note**: You can add or remove form elements only within the form block.

Form Settings
-------------

Once your form is built, configure its behavior in the **Form Settings** panel.

![Form Settings in Droip](https://droip.com/wp-content/uploads/2023/03/Form-Settings.webp)

**Name**: Assign a unique name to identify the form (e.g., “ContactForm”).

**Actions**: Define what happens on submission:

* **Email**: Send entries to an email address.
* **Webhook**: Send data to an endpoint (for integrations like Zapier or CRMs).

Learn more about [Form Actions](https://droip.com/docs/form-actions/).

**Store Form Data**: Enable to save submissions directly in Droip’s Form Data Manager.

**Max IP Entries**: Limit how many times a single IP can submit the form (e.g., set to “1” for one-time entry).

**Response Limit**: Set a maximum number of total submissions (useful for limited offers or registrations).

**After Submit**: Choose post-submission behavior:

* **None**: No extra action
* **Show Notification**: Display a success or failure message
* **Popup**: Trigger a popup (you can set different popups for success and failure)
* **Page**: Redirect to another page
* **External URL**: Redirect to an external website

Each “After Submit” action, Droip lets you define different experiences based on the form’s submission result:

**Default (None)**: The form’s normal state before submission.

**Success**: Shown if the form is submitted successfully (e.g., showing a success notification or popup).

**Fail**: Shown if the form submission fails (e.g., showing an error notification or popup).

You can customize the message, design, or triggered action for each state depending on the “After Submit” option you’ve selected, letting you control both what happens and how it looks for each scenario.

Customizing Form Elements
-------------------------

### Input Field

![Customizing Input Field in Form](https://droip.com/wp-content/uploads/2023/03/Input-Field-Settings.webp)

Click an input field to access the **Input Field Options**:

**Type**: Specify input type (text, email, password, number, date, etc.)

**Name**: Assign an internal name for data tracking

**Character Limit**: Set a max number of characters (text inputs only)

**Placeholder**: Add guidance text inside the field

**Required**: Mark the field as mandatory

Text Area
---------

![Customizing Text Area in Form](https://droip.com/wp-content/uploads/2023/03/Text-Area-Settings.webp)

Click a textarea to access its options:

**Name**: Assign a unique name

**Placeholder**: Add guidance text

**Required**: Mark the field as mandatory

### Select

![Customizing Select Field in Form](https://droip.com/wp-content/uploads/2023/03/Selector.webp)

Click the select element on the form to access its options:

**Name**: Assign an internal name. This name is used when processing form submissions (e.g., mapping the selected value).

**Options**: Add the choices that users can select. Click + Add to add new options. Reorder options easily by dragging them.

**Multiple Select**: Allow users to select multiple options (or disable for single selection)

**Required**: Make selection mandatory

Checkbox Input
--------------

![Customizing Checkbox Input Field in Form](https://droip.com/wp-content/uploads/2023/03/checkbox-input-settings.webp)

Inside the checkbox element, you’ll find:

* Checkbox Input element
* Text element

When you click the **Checkbox Input**, the **Checkbox Options** panel appears:

Here you can configure:

**Name**: Assign an internal name to track the checkbox.

**Value**: Set the value that will be submitted when the checkbox is checked.

**Checked by Default**: Enable this to have the checkbox pre-selected.

**Required**: Mark the field as mandatory (users must check it to submit).

Radio Button
------------

![Customizing Radio Button](https://droip.com/wp-content/uploads/2023/03/radio-button-1024x616.webp)

Click the **Radio Button** element to configure:

**Name**: Assign a name; this is used during form submission to collect the selected value.

**Options**: Add, edit, duplicate, delete, or reorder choices

![Manage the Radio field options in Droip ](https://droip.com/wp-content/uploads/2023/03/radio-button-required.webp)

Each option lets you specify:

![Set the content and value of radio fields](https://droip.com/wp-content/uploads/2023/03/option-settings.webp)

* **Content**: The visible label, what users will see (e.g., “Option A”)
* **Value**: The actual data on form submission (e.g., “A1”)

**Required**: Make selection mandatory

### Form Button

![Form Button in Droip](https://droip.com/wp-content/uploads/2023/03/form-button-settings.webp)

When you select the **Submit Button** in your form, the Submit Button Options panel opens. This panel lets you define what happens after someone submits the form.

Under the **Submit** dropdown, you can choose one of four actions:

**Success Message** – Shows a success message on the page after submission. You can enter the message in the **Message** field.

**Go to Page** – Redirects users to another page in your project once the form is submitted.

**Open Popup** – Opens a popup window after submission. Make sure you’ve already created the popup and linked it properly.

**External URL** – Redirects users to an external website after submitting the form.

reCAPTCHA
---------

![reCAPTCHA options in Droip forms](https://droip.com/wp-content/uploads/2023/03/rechaptcha.webp)

Click on the **reCAPTCHA** element on the form to configure:

**Enable reCAPTCHA**: Toggle on/off

**Version**: Choose reCAPTCHA version

**Site Key**: Enter your reCAPTCHA site key

File Upload
-----------

![File Upload Options in Droip Forms](https://droip.com/wp-content/uploads/2023/03/file-upload-settings.webp)

Click on the **File Upload** element on the form to configure:

**Name:** Give your file upload field a name for identification.

**Size**: Define the max file size.

**Select File Types**: From this dropdown, select which file types the user will be allowed to upload:

* Default: Supports all
* Document: .doc, .pdf, .txt
* Image: .jpg, .png, .gif
* Video: .mp4, .mov

Style Form Field Focus State
----------------------------

![Style Droip Forms for Different States](https://droip.com/wp-content/uploads/2023/03/Style-Form-Field-Focus-State.webp)

Highlight the focused state of input fields when users click on them or use the keyboard to fill them in. To access the focused state:

1. Select the input field.
2. Go to the Style Panel on the right sidebar.
3. Select Focused from the States.

Now, you can add a border, change the background color, and style as you wish. This styling will be visible when the input form field is in the focus state only.

Droip also provides a dedicated WordPress dashboard to manage your form data efficiently. To learn how to manage your form data in Droip, refer to [Form Data](https://droip.com/docs/form-data/) documentation.

---

<!-- Source URL: https://droip.com/docs/headings/ -->

---

Heading

**Headings** are titles and subtitles you want to display on your webpage. It is defined with the H1 to H6 tags with H1 defining the most important heading and H6 defining the least important heading.

Why Do You Need to Use Headings
-------------------------------

Search engines use headings to index the structure and content of your web pages.

Users often skim a page by its headings. It is important to use headings to show the document structure.

H1 headings should be used for the main headings, followed by H2 headings, then the less important H3, and so on.

How to Add Headings
-------------------

To add a Heading element:

1. Head over to the `Insert` > `Elements` panel and go to the `Basic` seciton.
2. Then drag and drop the `Heading` element to where you want it on your page.
3. Finally edit the text and customize it using the style options.

How to Style Headings
---------------------

![How to Style Headings](https://droip.com/wp-content/uploads/2023/02/How-to-Style-heading-1.webp)

In Droip, there are 6 levels for Headings ranging from largest to smallest: H1, H2, H3, H4, H5, and H6.

You can set H1 or H2 directly from the inline editor. The rest you can set from `Heading Options` which you can access by clicking on the ellipsis icon.

You can then style your Heading element using the options in the Style panel.

To do so, double-click on the Heading to edit the content, then use the Style panel on the right side to edit font, font size, font weight, color, etc from Typography.

Once you are happy with the styling, you can give it a class name to [reuse the style](https://droip.com/docs/class-manager/) for later.

AI-Generated Headings
---------------------

![AI-Generated Headings](https://droip.com/wp-content/uploads/2023/02/Ai-Gen.-Heading.webp)

For all text type elements including Heading, Droip has a nifty tool that you can use to generate text content automatically with the help of an AI. This will help you in saving significant time and effort in crafting compelling headings for your webpage.

Learn more about [AI Generator](https://droip.com/docs/ai-generator/).

---

<!-- Source URL: https://droip.com/docs/installation-update/ -->

---

Installation & Update

In this document, you’ll find a step-by-step guideline on installing Droip as well as activating its license.

Installing Droip
----------------

To install Droip, visit the [Droip Website](https://droip.com/) and create an account. Then from the [Pricing Page](https://droip.com/pricing/), choose the plan best suited for you and make your purchase.

Once you’re done with the purchase, you will find it listed on your `Subscriptions` page. Click on the `Download` button beside your Droip package to get the plugin in the form of a zip file. Then to install it, do the following:

1. Visit your WordPress Site’s Backend Dashboard.
2. Then go to `Plugins` > `Add New` and click on the `Upload Plugin` button.
3. Once on this page, click on the `Choose File` button and locate & select your plugin zip file.
4. Finally, once the file is uploaded, click on `Install Now`.

After it’s successfully installed, `Activate` your plugin.

### License Activation

Once you’ve installed and activated the Droip plugin, it’s time to activate its license. To do so, navigate to `WP Backend Dashboard` > `Droip` > `License Key`.

Here, enter the license key in the text field and click on the `Activate` button. To find your license key, login to your Droip account and navigate to `Subscriptions` where you’ll see it listed. You can also directly add your website and activate your license from this page too.

And you’re done! Now you’re all set to start designing a beautiful & interactive website using Droip Pro.

Also, if you’re facing any issues during the installation or while activating your license, contact us at **[[email protected]](/cdn-cgi/l/email-protection)**.

How to Update Your Droip Version
--------------------------------

To update your Droip Version, visit `WordPress Dashboard` > `Plugins` and locate Droip. If an update is available, it’ll be listed here. Click on the `Update Now` button to start updating.

---

<!-- Source URL: https://droip.com/docs/color-settings/ -->

---

Color Settings

Color your Typography, Backgrounds, Stroke, and more in any way you desire using Droip’s highly sophisticated Color options!

Use these settings to give your elements’ text or background a simple solid color. Or, go all out by using any one of three gradient styles to add an extra flair to your element!

Color Picker
------------

![Color picker ](https://droip.com/wp-content/uploads/2023/09/Color-Picker-2.webp)

Using Color Picker, you can choose a solid color for your element’s style. To open, simply select the element and go to the relevant section on the Style Panel that you want to customize (Typography, Background, etc), and click on the Color option.

### Pick a Color

To pick a color, do one of the following:

* Drag the rainbow color slider to a hue of your choice and select a shade from the color canvas.
* Or simply enter the color value in the field below. Use the dropdown to select HEX or RGB format.

### Set Opacity

![Set opacity ](https://droip.com/wp-content/uploads/2023/09/Set-Opacity.webp)

You can also use the second color slider to adjust your color’s opacity. You should be able to see its percentage value displayed on the right of the color value input field.

### Contrast Ratio

![Contrast ratio](https://droip.com/wp-content/uploads/2023/09/Contrast-Ratio-Button-Active.webp)

When you choose any color, you’ll also be able to see the color **Contrast Ratio** and the **WCAG** (Web Content Accessibility Guidelines) rating from the Color Picker.

This will make it easier to ensure that your page’s design is accessible and user-friendly.

You can also use the toggle on the right to see the contrast ratio division lines. These can help you easily identify the low-contrast, mid-contrast, and high-contrast colors.

### Color Swatch

![Color swatch](https://droip.com/wp-content/uploads/2023/09/Color-Swatch.webp)

Lastly, we have the Color Swatch where you can add colors to create your own Color Palette. This will make it easier for you to access the colors that you frequently need throughout the design process.

To add one, select your color and then click on the **+** icon at the bottom. The swatch works like a queue where you’ll be able to add up to seven colors and once you cross this limit, the oldest saved color will be removed from the swatch to make space for a new one.

Gradients
---------

Now let’s go over the three Gradient variations we have available:

* **Linear:** Gradient with color transition in one direction based on a defined angle.
* **Radial:** Gradient with color transition in the shape of a circle i.e. radiating from the center.
* **Conic:** Gradient with color transitions rotated around a center point.

![Available gradients](https://droip.com/wp-content/uploads/2023/09/Gradients.webp)

To access the Gradient panels, open the dropdown in the top left corner and select any one of the three gradient styles.

### Linear Gradient

![Linear gradient](https://droip.com/wp-content/uploads/2023/09/Linear-Gradient.webp)

On the Linear Gradient window, you’ll see the usual features like the color canvas, color sliders, etc. What’s new here is the Gradient Ramp.

**Picking a Color for a Color Stop:**

To pick a color, click on any color stop to select it, and then choose your color using either color sliders and the color canvas or by directly defining the color code.

Repeat the same process to pick colors for all the other color stops.

**Adding a Color Stop:**

By default, you should have two color stops (start & end) to work with but you can add more by clicking anywhere on the gradient ramp.

You can remove these extra stops by selecting them and pressing the delete button.

You can also drag the color stops along the ramp to adjust the location from where they’ll start or end.

**Setting the Angle:**

You should notice that the gradient ramp overlays a circular shape marked with the angles 0, 90, 180, and 270 degrees. By default, the angle is zero i.e. the gradient is horizontal. To change it, simply grab any one of the ends of the gradient ramp and drag it up or down.

The circle shape will reflect all of these customizations you apply to your gradient so you’ll be able to see what it will look like.

**Repeat:**

Right below the color sliders, you should notice a new toggle called Repeat.

When the “Repeat” option is enabled, the gradient pattern will repeat itself seamlessly, creating a continuous effect.

This means that for a Linear Gradient, suppose you have two color stops at the start and end points, enabling “Repeat” will cause the gradient to repeat in a seamless manner as it progresses beyond the endpoint, creating a repeating pattern.

### Radial Gradient

![Radial gradient](https://droip.com/wp-content/uploads/2023/09/Radial-Gradient.webp)

Next, we have Radial Gradient. Here, you’ll once again see familiar tools as well as the Radial Gradient tool. This tool, while looking very different, works similarly to the Linear Gradient tool.

**Picking a Color for a Color Stop:**

To pick a color, simply click on any color stop to select it. Then choose your color using the usual methods. Repeat the same process to pick colors for all the other color stops.

**Adding a Color Stop:**

By default, you should have two color stops (start & end) to work with. To add more, simply click anywhere on the gradient ramp.

And to remove a color stop, just select it and press the delete button.

**Adjusting the Centerpoint & Spread:**

To change the position of the gradient’s center point (starting point), click on the center handle and drag it as shown above.

And to adjust how much the gradient should spread outwards, click & drag the two end-points. Dragging the vertical handle will adjust the vertical spread and dragging the horizontal handle will adjust the horizontal spread.

**Repeat:**

Right below the color sliders, you should notice a new toggle called Repeat.

When the “Repeat” option is enabled, the gradient pattern will repeat itself seamlessly, creating a continuous effect.

Similar to Linear Gradient Repeat, for Radial Gradient, enabling “Repeat” will cause the same set of color stops to repeat in a seamless manner as it progresses beyond the endpoint, creating a repeating pattern but radiating from the center instead.

### Conic Gradient

![Conic gradient](https://droip.com/wp-content/uploads/2023/09/Conic-Gradient.webp)

Finally, we have the Conic Gradient and this time the gradient ramp is circular with the preview modal at its center instead of along the gradient bar.

**Picking a Color for the Color Stop:**

Select any one of the color stops and then pick a color of your choice using any of the methods discussed here. Do the same to pick colors for the other color stops.

**Adding a Color Stop:**

By default, you should have two color stops (start & end) to work with. So to add more color stops, simply click anywhere on the gradient ramp circumference.

📝 **Note:** For Conic Gradient, the ending color stop may not be visible at first as the starting color stop usually overlaps it. To adjust the ending color stop’s position, click and drag over the starting color stop to separate the two and place it at an angle of your choice.

**Adjusting Color Stop Position:**

To adjust the color stop position, simply click and drag the color stop in question and place it at an angle of your choice around the gradient ramp’s circumference.

**Off-Centered Conic Gradient:**

To make your conic gradient off-centered, click and drag the center point handle to reposition it where you want it.

**Reposition All Color Sops:**

To reposition the angle of all of the color stops, simply click and drag the end-point of the gradient bar around the gradient ramp’s circumference.

**Repeat:**

Right below the color sliders, you should notice a new toggle called Repeat.

When the “Repeat” option is enabled, the gradient pattern will repeat itself seamlessly, creating a continuous effect.

Unlike Radial Gradient, enabling “Repeat” for Conic Gradient will cause the gradient to repeat with the color transitions rotated around a center point.

---

<!-- Source URL: https://droip.com/docs/visibility-conditions/ -->

---

Visibility Conditions

![Droip Visibility Conditions](https://droip.com/wp-content/uploads/2025/05/1-droip-visibility-conditions.webp)

Visibility Conditions in Droip is a handy feature that lets you control which elements are visible on your website based on specific user criteria.

For instance:

* You can display a menu item in the navbar only for users with admin access.

* Or show an exclusive deal for users who signed up during a special promotional campaign.

These are just a few of the many ways Visibility Conditions can help you create personalized, user-focused experiences.

Why Use Visibility Conditions
-----------------------------

Not all users should see the same content, and Visibility Conditions in Droip help you manage this effortlessly.

Whether you’re restricting content based on user roles for added security, showing specific content to users who registered during a certain time, or personalizing content based on any other user-specific criteria, Visibility Conditions help you control exactly who sees what on your website.

This makes for a personalized, more relevant experience for users and a more secure website on your end.

Applying Visibility Conditions to Elements
------------------------------------------

From the Droip editor, head to the **Style Panel** to access **Visibility Conditions**.

### Adding a Visibility Condition

![Adding a Visibility Condition](https://droip.com/wp-content/uploads/2025/05/2-droip-adding-a-visibility-condition.webp)

To add a Visibility Condtion, follow these steps:

**Step 1**: Click on the **+ icon** to add a new condition.

**Step 2**: From the **Field** dropdown, select **User**, then choose the data field you want to base your condition on.

**Step 3**: Then, from the **Operator** dropdown choose the comparison type and from the **Value** dropdown select the value to compare against.

**Step 4**: Click **Save** to apply the condition.

### Adding Multiple Conditions

You can also stack multiple conditions using AND (where all conditions must be true) or OR (where any condition can be true) to further fine-tune when elements should be shown.

**Adding ‘AND’ Conditions**

![Adding ‘AND’ Conditions](https://droip.com/wp-content/uploads/2025/05/3-droip-adding-an-and-visibility-condition.webp)

To stack multiple AND conditions, do the following:

**Step 1**: After adding your first condition, click on the **+ Add Rule** option.

**Step 2**: Set the next condition as usual and hit save.

Repeat these steps to add more AND conditions.

**Adding ‘OR’ Conditions**

![Adding ‘OR’ Conditions](https://droip.com/wp-content/uploads/2025/05/4-droip-adding-an-or-visibility-condition.webp)

To stack multiple OR conditions, do the following:

**Step 1**: After adding your first condition, click on the **+ icon** on the top right.

**Step 2**: Set the next condition as usual and hit save.

Repeat these steps to add more OR conditions.

### Editing a Visibility Condition

![Editing a Visibility Condition](https://droip.com/wp-content/uploads/2025/05/5-droip-editing-a-visibility-condition.webp)

You can, of course, edit your conditions at any time.

To edit a condition, follow these steps:

**Step 1**: Click on the condition you want to edit. This will reopen the Visibility Conditions settings.

**Step 2**: Make your changes and hit save.

### Removing a Visibility Condition

![Removing a Visibility Condition](https://droip.com/wp-content/uploads/2025/05/6-droip-removing-a-visibility-condition.webp)

Lastly, to remove a condition, do the following:

**Step 1**: In the **Visibility Conditions** panel, find the condition you want to remove and click the – icon next to it.

And you’re good to go!

### Applying Visibility Conditions To Dynamic Content

![Applying Visibility Conditions To Dynamic Content](https://droip.com/wp-content/uploads/2025/05/7-applying-visibility-conditions-to-dynamic-content.webp)

You can also apply visibility conditions to dynamic content, whether it’s part of a collection list or a single-page template based on **Post** fields.

Here’s what you have to do to implement it:

**Step 1**: Select the element you want to show or hide.

This could be:

* The entire collection element
* A specific element within the collection
* Or an element within a single-page template

**Step 2**: Once selected, add a new visibility condition from the style panel.

**Step 3**: From the **Field** dropdown, now you’ll see an option called **Post**. Choose this to access the collection fields you want to base your condition on.

**Step 4**: Then, as usual, from the **Operator** dropdown, choose the comparison type, and from the **Value** dropdown, set the value to compare against.

**Step 5**: Click **Save** to apply the condition.

And just like that, you can create visibility conditions based on dynamic post collection fields!

This comes in handy in various ways, such as to show a “Featured” ribbon if the post item’s featured field is toggled “On”, hide limited-time offers based on the date once it expires, and so on.

---

<!-- Source URL: https://droip.com/docs/button/ -->

---

Button

Buttons are essential elements in web development used to prompt user actions, such as submitting forms, canceling operations, or navigating to different pages. This guide will walk you through how to add and customize buttons using Droip.

Adding a Button
---------------

To add a button to your web page, follow these simple steps:

1. Open the `Elements` panel on the right sidebar.
2. From the top panel, navigate to `Elements` > `Basic`.
3. Drag and drop the `Button` element onto the canvas.

Customizing the Button
----------------------

With Droip, you have full control over the appearance of your buttons. You can easily customize various properties to match your brand’s identity and engage your users effectively.

### Changing Button Text & Font

To edit the button text, simply double-click on the text to start editing. To modify the font and other typography styles, use the `Style` panel on the right sidebar.

You can also change the text color, style, and contrast ratio from the `Button Inline` editor.

![Changing Button Text & Font](https://droip.com/wp-content/uploads/2023/09/Change-Button-Text-Font.webp)

### Changing Background Color

To add a background color to the button, follow these steps:

1. Go to the `Style` panel on the right sidebar.
2. Scroll down to `Backgrounds`.
3. Choose a color from the color picker to set the background color.

![Changing background color](https://droip.com/wp-content/uploads/2023/09/Change-Background-Color.webp)

### Changing Corner Radius

![Change corner radius of a button](https://droip.com/wp-content/uploads/2023/09/Change-Corner-Radius.webp)

The `Corner Radius` defines whether the border corners are rounded or straight. You can adjust the Border Radius using the slider or input field to set the value in pixels or percentage.

For further customization, you can set the border radius for each corner individually by clicking on the dot icon.

Adding a Button Link
--------------------

Buttons can serve as links to various destinations. You can link a button to the following:

![Adding a button link](https://droip.com/wp-content/uploads/2023/09/Adding-a-Button-Link.webp)

* **Web Address:** Enter the URL of the page you want to link to in the field below. Tick the checkbox to enable **Open in New Tab**.
* **Email:** To link an Email, enter the Email address and the Subject in the available fields.
* **Phone Number:** Enter the Phone Number you want to link along with its country and area code in the following field.
* **Page:** Select the Page you want to link from the following drop-down list and tick the checkbox for it to **Open in New Tab**.
* **Section:** Type in the Section Id in the text field below to link to a particular Section that is on this page.
* **Pop-up:** Select the Pop-up you want to link from the following drop-down list.

Changing Button Color on Hover/Focus State
------------------------------------------

Enhance the user experience by changing the button color when transitioning between none and hover/focused state.

To change the background color on hover:

* Go to `Style Panel` > `Class & Sub-class` > `States Menu` and select **None**.
* From the background section, select a color from the color picker.
* Again, go to `Style Panel` > `Class & Sub-class` > `States Menu` and select **Hover**.
* From the background section, select a different color from the color picker.

Creating a Download Button
--------------------------

Download buttons are another necessary feature of any webpage. To create a download button, follow these steps:

1. Copy the source `URL` of the file you want users to download. Ensure that the URL is the complete link address, not a shortened version.
2. Select the button you want to use as the download button and access the `link settings`.
3. Choose `Web Address` as the link type.
4. Paste the copied URL into the provided field in the link settings.
5. Close the link settings window and `preview` your webpage. Clicking on the button should initiate the file download.

For further customization, you can utilize the [custom attributes](https://droip.com/docs/custom-properties/) feature of Droip to customize the name of the downloaded file.

---

<!-- Source URL: https://droip.com/docs/dropdown/ -->

---

Dropdown

Dropdown provides toggleable and contextual overlays for presenting lists of links and other content. In Droip, a **Dropdown** is a nifty element that allows you to add dropdown menus anywhere on your page.

Adding a Dropdown
-----------------

To add a **Dropdown** element, do the following:

1. Open the `Elements` panel.
2. Scroll down to the `Components` section.
3. Drag & drop the `Dropdown` element onto your canvas.

Configuring the Dropdown
------------------------

The Dropdown element comprises two fundamental components: the Dropdown Trigger and the Dropdown Target.

### Dropdown Trigger

The **Dropdown Trigger** serves as the interactive element that users engage with to activate or open the dropdown menu. Upon clicking or hovering over the Dropdown Trigger, the dropdown menu appears, showcasing available options for users to select.

By default, the Dropdown Trigger includes both text and an icon element. Nevertheless, you can add any preferred element as the dropdown trigger.

### Dropdown Target

The **Dropdown Target** refers to the area or container responsible for containing the content of the open dropdown menu. This region showcases the list of choices or supplementary content after the Dropdown Trigger’s activation.

To access the Dropdown Target, configure the `State` option to `Show` within the Dropdown Settings, elaborated on in the next section.

Dropdown Settings
-----------------

* **Open on**: Determine whether the dropdown content opens on **Hover** or **Click**.
* **Animation**: Define the animation that governs how the dropdown content enters the screen. This includes options like sliding from the left, fading in, or expanding from a smaller to a larger size.
* **Easing**: Easing refers to the rate of change of an animation’s speed. It controls the acceleration and deceleration of the animation, affecting its overall smoothness. Options typically include linear, ease-in, ease-out, and ease-in-out. Choose the easing function that best complements your animation’s style.
* **Delay**: Specify the duration before the animation commences, measured in seconds or milliseconds.
* **Duration**: Indicate the animation’s length.

Learn more about [Animation & Interaction](https://droip.com/docs/style-panel-overview/).

* **State**: Toggle the State to `Show` to render the Dropdown Target visible, and `Hide` to conceal it.

Styling the Dropdown
--------------------

Once you’re done creating your dropdown you can add style customization using the Style Panel located at the ride side.

---

<!-- Source URL: https://droip.com/docs/svg/ -->

---

SVG

**Scalable Vector Graphics (SVG)** is an XML-based vector image format for 2D graphics with support for interactivity and animation.

Why Use SVG Shapes?
-------------------

There are several reasons why you might want to use SVG shapes on your website:

1. **Scalability**: SVG shapes are vector-based, which means they can be scaled to any size without losing quality. This is especially useful when creating graphics that need to be displayed on different devices with different screen sizes.
2. **Interactivity and Animation**: SVG shapes can be animated and made interactive, making them a great choice for creating dynamic graphics and user interfaces.
3. **Small File Size**: SVG shapes are usually smaller in file size than bitmap images, which can improve your website’s loading speed.
4. **Accessibility**: SVG shapes can be made accessible for users with disabilities, for example, by adding descriptive text for screen readers.
5. **Style Control**: You can easily control the appearance of SVG shapes making it easy to match your website’s style and brand.
6. **Reusability**: You can reuse SVG shapes across multiple website pages, saving time and resources compared to creating multiple images.

These are just a few of the benefits of using SVG shapes on your website. By using SVGs, you can create visually appealing, fast-loading, and interactive graphics that enhance the user experience on your website.

SVG Elements
------------

In Droip, we have two elements that are in the SVG file format. They are:

* **Icon** element
* **SVG** element

So let us go over how you can add and use these for your website.

### How to Add Icons

1. Add the `Icon` element to your canvas.
2. Click on `+Add From Media` to open the Icon Library in the Media Manager
3. Choose from a wide selection of icons provided by Droip.

📝 **Note:** Keep in mind that these Icons are fetched from a local pool and not from an external library that’s been called. This means that your Icon load time will be that much faster.

To learn more about the Icon Library, check out its section on the [Media Manager](https://droip.com/docs/media-manager/) documentation.

### How to Add SVG Shapes From Media

1. Place the `SVG` element on your canvas.
2. Click on `+Add From Media` to open the Clip-Path & Shape editor, which is also accessible from the Media Manager.
3. Under `SVG Shapes`, select a shape that suits your needs.
4. Customize the shape by dragging its control points (vertices) to adjust or add more vertices as required.
5. Use the right side panel to modify attributes such as Fill, Stroke Color, and Stroke Weight.

On the right side panel you’ll find the following options:

* **Fill:** Set the color & the opacity of your shape from here.
* **Stroke Color:** Set the color & the opacity of your shape’s outline from here.
* **Stroke Weight:** Set the weight of the stroke by entering into the field below the Stroke Color toggle.

### How to Add SVG Shapes Using Paste SVG

1. Open your SVG file using your preferred IDE and copy its code.
2. Then, select the SVG element and click on the `Paste SVG` option from the inline editor.
3. Finally, paste the code and click on `Update`.

### Uploading SVG Files

![Uploading SVG Files](https://droip.com/wp-content/uploads/2023/03/Uploading-SVG-Files.webp)

If you want to upload and use your own SVG files in your designs and layouts, you can do that as well.

To do that, you have to first enable the `SVG Upload` option from **Droip WordPress dashboard** > **Settings** > **General**.

---

<!-- Source URL: https://droip.com/docs/form-actions/ -->

---

Form Actions

In Droip, **Form Actions** let you control exactly how submissions are handled, whether you want to notify your team, confirm submissions to users, or send data to other apps in real-time.

This guide will walk you through:

* Configuring SMTP to ensure reliable email delivery
* Setting up Email Actions to send notifications and automated responses
* Using Webhooks to integrate your forms with CRMs or automation tools

Email Actions in Droip Forms
----------------------------

In Droip, Email Actions let you define how form submissions are sent and handled. You can:

* Send **Admin Notifications** — receive a copy of every form submission.
* Send **Automated User Emails** — confirm to users that their submission has been received.

Before setting up, it’s important to understand the basics:

* **SMTP (Simple Mail Transfer Protocol)** ensures emails are sent through a proper mail server instead of PHP mail, reducing the chances of messages being marked as spam.
* **Email Action in Droip** determines where submissions go, how they appear, and who receives replies.

### Setting Up SMTP for Gmail

If you plan to use Gmail to send emails from your form:

**Step 1: Enable 2-Step Verification**

1. Go to your [Google Account Security](https://myaccount.google.com/security) page.
2. Find 2-Step Verification and turn it on.

**Step 2: Create an App Password**

1. After enabling 2-Step Verification, go to [App passwords](https://myaccount.google.com/apppasswords).
2. Name your app like “WordPress” or “Droip.”
3. Copy the 16-character password generated. Please note this is your SMTP password (not your normal Gmail password).

**Step 3: Enter SMTP Settings in Droip**

Navigate to `Droip Editor` > `Apps` > `SMTP` and configure:

* Host: [smtp.gmail.com](http://smtp.gmail.com)
* Port: 587 (with TLS/STARTTLS) or 465 (with SSL)
* Encryption: TLS for 587 / SSL for 465
* Username: [[email protected]](/cdn-cgi/l/email-protection#1d6472686f3078707c74715d7a707c7471337e7270)
* Password: 16-character App Password from Google
* Sender Email: [[email protected]](/cdn-cgi/l/email-protection#423b2d37306f272f232b2e02252f232b2e6c212d2f)
* Sender Name: Your name or company name

### Configuring Droip Form Email Actions

Once SMTP is set up, you need to configure your form to send emails properly.

**Step 1: Open Form Email Action Settings**

1. Select your form on the canvas.
2. Open `Form Settings` > `Actions` > `+ Add` > `Email`

**Step 2: Setup Email Action**

* **Recipient:** Set Recipient to [admin\_email] for admin notifications, or [email] if your form includes a user email field. Do **not** leave it as [email] unless your form has an email field.

* **Reply To:** [email]. This ensures that when you click “Reply” in your inbox, the response goes directly to the user who submitted the form.
* **Name:** [first\_name] (optional).
* **Subject:** Enter a subject for your email, e.g, New Contact Form Submission.
* **Email body: You can include field names to write your email body.**

**Example**:

> Hi [first\_name],
>
> Thank you for reaching out! We have received your message:
>
> [message]
>
> Our team will get back to you shortly.

### Testing Your Setup

1. Fill out your form on the website.
2. Confirm that the email arrives at the recipient address.
3. Click “Reply” to verify it goes to the user’s email.
4. If emails do not appear, check your Spam/Junk folder.

Webhooks in Droip Forms
-----------------------

A Webhook is a way for your form to send data to an external URL in real-time whenever a submission occurs. Unlike email, which simply delivers a message, webhooks allow you to integrate your form with other apps or services, such as:

* CRM systems (e.g., HubSpot)
* Automation tools (e.g., Zapier)
* Analytics or database platforms
* Custom server endpoints for processing submissions

### How to Set Up a Webhook in Droip

1. Open `Form Settings` > `Actions` > `+ Add` > `Webhook`
2. Enter the `URL` of the service or endpoint you want to send data to.
3. Select the HTTP Method:  
   * **GET**: Sends data as query parameters in the URL.
   * **POST**: Sends data in the request body (recommended for most integrations).
4. `Save` the webhook.

---

<!-- Source URL: https://droip.com/docs/upload-custom-fonts/ -->

---

Font Library

Using a variety of fonts is essential for web design, and the ability to upload custom fonts adds even more flexibility.

To access the `Font Library`, click on the **dropdown icon** next to Droip’s logo in the **Topbar**.

![Font Library in Droip](https://droip.com/wp-content/uploads/2023/02/Font-Library.webp)

Font Library Tabs
-----------------

The Font Library consists of three main tabs:

![Font Library Tabs in Droip](https://droip.com/wp-content/uploads/2023/02/font-library-tabs.webp)

### 1. Google Fonts

This tab provides access to a wide range of open-source fonts from **Google Fonts**. You can select and incorporate these fonts into your project for use in website text, branding elements (including logos), and more.

### 2. Installed Fonts

The **Installed Fonts** tab displays a list of all fonts that are already installed in your project. If you need to remove any fonts, simply click the **Remove** button located at the bottom-right corner.

### 3. Custom Fonts

This tab allows you to **upload and use your own custom fonts** in your Droip projects, giving you full creative control over typography.

📝 **Note**: You can also access the **Font Library** from the **Typography** panel under the **Font** dropdown.

![Access Font Library from Typoghraphy](https://droip.com/wp-content/uploads/2023/02/access-font-library.webp)

How to Upload Custom Fonts
--------------------------

Follow the steps below to upload and integrate custom fonts into your webpage.

![Upload Custom Font in Droip](https://droip.com/wp-content/uploads/2023/02/upload-custom-font.webp)

1. From the Font Library and select `Custom Fonts`.
2. On the right-hand side, you’ll find a link to the **Font Squirrel Webfont Generator**. Click on it.
3. Upload your **.OTF** or **.TTF** file to the Font Squirrel Webfont Generator.
4. Choose between **Basic** or **Optimal** settings. Advanced users can explore **Expert** settings.
5. Confirm your legal rights to use the font for web embedding by checking the eligibility box.
6. Download the **Webfont Kit zip file**.
7. Return to Droip and click **Upload From Computer** to upload the Webfont Kit.

Using Your Custom Fonts
-----------------------

![Using Custom Font in Droip](https://droip.com/wp-content/uploads/2023/02/using-custom-font.webp)

To apply your uploaded custom fonts in your project:

1. Select the **text element** where you want to use the custom font.
2. Go to **Style Panel > Typography**.
3. Under the **Font** dropdown, your custom fonts will appear alongside the available fonts.

With the **Font Library**, you can easily enhance your design with a wide selection of fonts or upload your own for a truly unique look.

---

<!-- Source URL: https://droip.com/docs/pages/ -->

---

Pages

The **Pages Panel** in Droip lets you create pages within your project. You can create new pages, add pre-made utility pages, browse and use templates, or create popups for various use cases.

![Pages Panel in Droip](https://droip.com/wp-content/uploads/2023/02/pages.webp)

Clicking the **`+`** button at the top opens a menu with four options:

* **New Page** – Create a new blank page.
* **New Utility Page** – Add pre-made utility pages like 404, password retrieval, login, and more.
* **New Template** – Add a template page to design once and apply across all items.
* **New Popup** – Create popups for modals, alerts, or promotional messages.

**Action Menu Options**
-----------------------

![Action Menu Options in Pages](https://droip.com/wp-content/uploads/2023/02/action-menu-settings.webp)

Click on the `ellipsis icon` (•••) beside each page to open the **Action Menu**, which includes the following options:

* **Settings** – Access the Page Settings panel.
* **Duplicate** – Create an exact copy of the selected page.
* **Rename** – Change the name of your page.
* **Preview** – View the page before publishing.
* **Import** – Import a Droip page in the form of a .zip file.
* **Export** – Export this page as a .zip file.
* **Delete** – Remove your page. A confirmation popup will appear before deletion.

**Applying Variable Mode**

![Accessing variable mode from pages](https://droip.com/wp-content/uploads/2023/02/applying-mode.webp)

Clicking on the Variable icon lets you apply the **Variables Mode** to the page. This allows you to maintain consistent brand styles across all your pages by applying the global variables you’ve set for the project.

Page Settings
-------------

The Page Settings panel is organized into the following tabs:

### General

![General Page Settings in Droip](https://droip.com/wp-content/uploads/2023/02/Page-Settings.webp)

The **General** tab allows you to define essential details about your page:

* **Title** – Set the page name.
* **Slug** – Edit the auto-generated page URL (slug) for better readability.
* **Page Description** – Provide a short description of your page.
* **Status** – Set the page status.

### SEO Settings

![SEO Settings in Droip](https://droip.com/wp-content/uploads/2023/02/SEO-settings.webp)

The **SEO** tab helps optimize your page for search engines. It includes:

* **SEO Title Tag** – Define the page title that appears in search results.
* **Meta Description** – Add a brief description to improve SEO.

📝 **Note:** If you have an **OpenAI API key** added, you can generate a **Meta Title** and **Meta Description** with AI in one click.

Use the Preview field to see how your page will appear on SERPs. Once satisfied, hit Save.

**Open Graph**

Customize how your page appears when shared on social media platforms:

* **Add Cover Image** – Upload a cover image to serve as a thumbnail.
* **Open Graph Title** – Set a title for your webpage.
* **Same As SEO Title** – Toggle to match the Open Graph Title with the SEO Title.
* **Open Graph Meta Description** – Provide a brief description.
* **Same As SEO Meta Description** – Toggle to match the Open Graph Meta Description with the SEO Meta Description.

### Custom Code

![Custom Code Option in Droip](https://droip.com/wp-content/uploads/2023/02/custom-code.webp)

In this tab, you can add Custom Code to your page, allowing further customization using advanced features. For more information on using Custom Code, refer to our [Custom Code Documentation](https://droip.com/docs/custom-code/).

Search & Filter Pages
---------------------

![Filter & Search Option in Pages](https://droip.com/wp-content/uploads/2023/02/Filter-pages.webp)

The Search & Filter options on top of the pages panel allow you to easily locate and organize pages within the project. With just a few clicks, you can quickly find the specific pages you’re looking for, making page management more efficient and streamlined.

**Migrate With Droip**
----------------------

Droip offers a seamless migration option for existing pages, allowing you to edit them in Droip without losing your content.

To migrate a page:

1. Open the page from the WordPress admin dashboad.
2. Click `Edit With Droip`on the top of the page editor.
3. A popup will appear with the message **Safely Migrate to Droip**.
4. Click `Convert` to retain your existing content.
5. The content will load on the Droip canvas, ready for editing.
6. To start fresh, click `Start From Blank` (this will erase all existing content, so proceed with caution).
7. Click `Back` on the popup to exit without making changes.

📝 **Note:** Starting from blank will delete all existing content permanently. Ensure this is your desired action before proceeding.

---

<!-- Source URL: https://droip.com/docs/custom-properties/ -->

---

Custom Properties

For every element, you’ll find the following Custom Properties options which you can access by clicking on the ellipsis icon from their inline editor.

Visibility
----------

**Visibility**: Use this option to show or hide your elements on the canvas. To show it, select `Visible` and to hide it, select `Hidden`.

Custom Attributes
-----------------

Custom Attributes allow you to enhance your standard HTML elements by adding additional information to define more characteristics. This comes in handy when you need to achieve specific functionalities that are not readily available through built-in options.

### How to Add a Custom Attribute

![How to Add a Custom Attribute in Droip](https://droip.com/wp-content/uploads/2023/03/How-to-Add-a-Custom-Attribute.webp)

To add a **Custom Attribute** to any element on your canvas, follow these steps:

1. Select the `element` you wish to modify.
2. Access the `inline editor` and click on the **settings** icon to open its settings.
3. Click on `Add New Attributes` to add a new attribute and specify its Name and Value.
4. The Name field should contain the name of the desired attribute (pre-defined in the system), while the Value field should contain any parameters associated with this attribute.
5. Press `Add` to save the custom attribute, and it will be listed in the settings window.

### Managing Custom Attributes

![Managing Custom Attributes in Droip](https://droip.com/wp-content/uploads/2023/03/Managing-Custom-Arrtributes.webp)

Click on the ellipsis icon beside any of the attributes on the settings window to access the **Edit** and **Delete** options.

### Custom Attribute Use Cases

There are many Custom Attributes available out there, and while we can’t cover them all, we’ve tried our best to highlight some useful ones that may come in handy in various situations.

**Adding Tooltips**

Tooltips provide context and purpose when users hover over elements. You can add a Tooltip to any element using Custom Attributes.

Select the element and access its settings. Open Custom Attributes and click on `Add New Attribute`.

![Custom Attribute Use Cases
](https://droip.com/wp-content/uploads/2023/03/Custom-Attribute-Use-Cases.webp)

Set the Name of the attribute as title and the Value as your Tooltip text, providing a brief definition or purpose. Hit `Add`, and the tooltip text will appear when users hover over the element

Now when you hover over your element, this tooltip text should appear.

**Turn Off Spellcheck**

You can also turn off spellcheck for any Input Field using the Custom Attribute feature.

![Turn Off Spellcheck Using Custom Attributes](https://droip.com/wp-content/uploads/2023/03/Turn-off-spellcheck.webp)

1. Select the text field element and open the `Input Field Options`.
2. Click on `Add New Attributes`.
3. Set the Name as **spellcheck** and the Value as **false**.
4. Hit `Add` to save this attribute, and the spellcheck will be turned off for the input field.

**Renaming A Download File**

Custom Attributes can also be used to rename files when users download them by clicking on a button or link:

![Renaming A Download File Using Custom Attributes](https://droip.com/wp-content/uploads/2023/03/Renaming-A-Download-File.webp)

1. Select the button or link element and access its settings.
2. Click on `Add New Attributes`.
3. Set the Name of the attribute as **download** and the Value to the desired **filename**.
4. Hit `Add`, and the file will be renamed accordingly upon download.

**Creating a Descending Ordered List**

To display Ordered Lists in reverse order, follow these steps:

![Creating a Descending Ordered List](https://droip.com/wp-content/uploads/2023/03/Creating-a-Descending-ordered-List.webp)

1. Select your Ordered List element.
2. Click on the ellipsis icon to open `List Options` and add a new attribute.
3. Set the Name of the attribute as **reversed** (parameter not needed) and click `Add` to save your attribute.
4. Your list will now be resorted in descending order.

### Summary

Custom Attributes offer vast possibilities for enhancing your website’s functionality and user experience. To explore even more ways to customize your elements, refer to the list of [All HTML Attributes](https://www.w3schools.com/tags/ref_attributes.asp) that you can use.

📝 **Note**: Do keep in mind that some of these attributes may already be in use for the built-in Droip features so do double-check in case that option is already available.

---

<!-- Source URL: https://droip.com/docs/class-manager/ -->

---

Class Manager

In Droip, a **Class** serves as a blueprint for creating objects, defining their structure, and initial style attributes.

On the other hand, a **Sub-class** is a child class that inherits the attributes of its parent class while also having the ability to possess its own unique characteristics.

Classes and Sub-classes
-----------------------

![Classes in Droip for consistent styles](https://droip.com/wp-content/uploads/2023/03/classes-in-droip.webp)

In Droip, using **classes** and **sub-classes** helps you manage and reuse styles efficiently across your website.

Whenever you customize the style of an element, Droip automatically creates a class to hold those style rules, eliminating the need to define them from scratch manually.

### Creating Classes

A **class** is a reusable style group applied to one or more elements. To create a class:

* Select an element.
* Make your styling changes (e.g., color, padding, typography).
* Droip will automatically assign a class to that element based on your changes.

You can also rename the class to something meaningful for easier identification and reuse.

### Creating Sub-classes

A **sub-class** builds upon an existing class with additional or overridden styles. It’s ideal for cases where you want to slightly tweak a base design without affecting all instances of the main class.

To create a sub-class:

* Select an `element` that already has a base class applied.
* Click on the `Classes` selector field and `create a sub-class` to preserve the base class while applying unique styles to this variation.
* Add or adjust styles as needed

This layered styling approach gives you granular control while maintaining consistency across your site.

### Editing a Class or Sub-class

![Editing a Class in Droip](https://droip.com/wp-content/uploads/2023/03/Editing-a-Sub-class.webp)

To edit a class in Droip:

* Simply `click on the class label` attached to the element.
* The selected class will be `highlighted`, and the background will **blur**, helping you focus on the active style scope.
* As you customize the element, any changes will be **automatically saved** to that class.
* These updates will instantly apply across **all elements using the same class**, ensuring consistency throughout your design.

### Duplicating Style Settings Using Classes

Droip’s class system allows you to efficiently duplicate and manage styles across multiple elements. Instead of manually recreating styles, you can simply apply existing classes or sub-classes to new elements.

**How It Works**

To make another element adopt the same style, just apply the same class or sub-class used in the original element. However, keep in mind that **sub-classes must be applied after their parent class**—this ensures proper inheritance and styling accuracy.

**Example Scenario**

Let’s walk through a practical example:

1. **You add a Heading element** to the canvas and begin customizing its style without creating a class manually.  
   * Droip automatically generates a class to store those style changes (e.g., Heading\_1).
2. **You add a second Heading** and want it to look the same.  
   * Go to the **Classes** panel and apply the class used in the first heading.
   * Now, both headings share the same style. Any updates to one will reflect in the other.
3. **You want the second Heading to look slightly different** (e.g., different color or font weight).  
   * Create a **sub-class** for the second heading (e.g., Heading\_1.bold).
   * This sub-class will override specific styles without affecting the original class or the first heading.
4. **You add a third Heading** and want it to match the second one (with both the base and modified styles).  
   * First, apply the base class (Heading\_1).
   * Then, apply the sub-class (Heading\_1.bold).
   * The third heading now shares both the foundational and modified styles.

### Managing Classes and Sub-classes

![Managing Classes in Droip](https://droip.com/wp-content/uploads/2023/03/Renaming-and-Removing-Sub-classes.webp)

You can easily **rename, detach, or remove a class**:

* Just `click the three-dot`(…) **icon** next to the class name in the Classes panel.
* From there, you can:  
  + **Rename** the class for better organization.
  + **Detach** the class to remove styling from the selected element without deleting it.
  + **Remove** the class entirely if it’s no longer needed in your project.

This lets you keep your styling system clean, consistent, and easy to manage.

Element States in Droip
-----------------------

![Element States in Droip](https://droip.com/wp-content/uploads/2023/03/States-Menu.webp)

Droip lets you fine-tune how elements look and behave in different interaction states—allowing you to create more dynamic, user-friendly experiences.

Here are the supported states:

**Neutral** This is the default appearance of an element when no interaction is taking place. It’s how the element looks when the page first loads.

**Hover** Triggered when a user places their cursor over an element without clicking. This is commonly used for buttons, links, and interactive components.

**Focused** This state is activated when a user navigates to an interactive element (like a button or input field) using the keyboard. It helps with accessibility and keyboard navigation.

These states can be styled individually in Droip, giving you control over how elements respond to different user interactions.

Using Pseudo Elements in Droip
------------------------------

![Using Pseudo Elements in Droip](https://droip.com/wp-content/uploads/2023/03/Pseudo-Class.webp)

Just below the **States Menu**, you’ll find the **Pseudo Element** dropdown. Droip supports **Pseudo Elements**, which let you style specific parts of an element that aren’t explicitly defined in the HTML.

These are especially useful for adding visual effects or enhancing form elements without extra markup.

**What Are Pseudo Elements?**

Pseudo elements let you style:

* Generated content (before, after)
* Specific element states (placeholder, checked, disabled, etc.)
* Structural conditions (empty)
* User interactions (active, visited)

**How to Use Pseudo Elements in Droip:**

1. Select the `element` you want to customize.
2. Go to the `States Menu`, then open the `Pseudo Element` dropdown.
3. Choose from the list of pseudo elements.
4. Apply your desired styles—these will only affect the element in the selected pseudo context.

Need more context? Refer to the [MDN Web Docs on Pseudo Elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements) for deeper explanations.

---

<!-- Source URL: https://droip.com/docs/style-panel-overview/ -->

---

Style Panel Overview

The Style Panel of Droip is basically where all of the magic happens. From here, you can customize every aspect of your element’s style.

![style-panel-overview](https://droip.com/wp-content/uploads/2023/05/Style-Panel-Overview.webp)

Located on the right side of the screen, you’ll notice that the Style Panel is made up of the following sections:

1. Class Manager
2. Typography
3. Structure
4. Size
5. Background
6. Stroke
7. Shadow
8. Effects
9. Position
10. Transform
11. Transition
12. Interaction

As you can tell from this list, you can customize your element’s typography, structure, background, and more from here. Not only that but you can also duplicate your style settings with the help of sub-classes and reuse them throughout your design process!

Class Manager
-------------

The Class Manager is where you can define **Classes** to duplicate and reuse the style settings of an element. This means you don’t need to manually customize each and every instance, saving your time and effort.

This is also where the **States Menu** is located and from here you can switch between the various **States** of an element and define its behavior and style for that state. With the help of this feature, you can design a highly responsive and interactive website.

The default States include **None**, **Hover** & **Focus**. However, you also get a range of other states known as **Pseudo Classes** to choose from.

You can also access the **Inheritance Menu** from here by clicking on the dropdown above the Selector field. This menu will show all of the parent and ancestor classes of this element and you can click on one to edit that class from here.

For more information about this section, check out the [Class Manager](https://droip.com/docs/class-manager/) documentation.

Typography
----------

Using Typography settings, you can ensure that your content is legible and visually appealing. From here you can adjust your text’s font, font size, font weight, alignment, and more.

Not just that but from the **Advance Font Editor**, you can access even more customization options. Take a look at the [Typography](https://droip.com/docs/typography/) documentation to learn more.

Structure
---------

From Structure, you can define how your element and the elements around it will be displayed on the canvas.

To change your element’s Structure, click on the dropdown that’s located here. You’ll find the following Structure types to choose from:

* Block
* Inline
* Inline Block
* None
* Flex
* Grid

You can also adjust your element’s Padding and Margin values from here. Simply click and drag any one of the sides to adjust them. You can match the values for all sides, or just some of them, or even define each one differently.

To learn more, check out our documentation on [Structure](https://droip.com/docs/structure/).

Size
----

As the name implies, using the settings from the Size section you can define the height, width, and Overflow of an element.

You can also set the **Minimum** and **Maximum** values for size as well as enable **Clip Content** from here. Please visit the dedicated documentation on [Size](https://droip.com/docs/size/) to learn more.

Background
----------

Next up we have Background settings and from here you can add **Solid**, **Gradient**, and **Image** type Backgrounds.

When it comes to Gradients, you can also choose between **Linear**, **Radial**, or **Conic** Gradient types.

You’ll also be able to **Clip Backgrounds** from here and this includes the **Text** option which is a nifty way to have Image Backgrounds adopt any text content’s shape!

To learn more, visit the [Background](https://droip.com/docs/background/) documentation.

Stroke
------

From the Stroke section, you can add a **Border** around any element. You can set this border’s size, color, and style.

You can also adjust any element’s **Radius** from here. This will curve the edges of your element to give it a more rounded look.

Similar to borders, you can add an **Outline** around your element too. Outlines are different from borders because they’re drawn outside the element’s edges instead of over them.

For more info, check out [Stroke](https://droip.com/docs/stroke/)’s documentation.

Shadow
------

Then we have the Shadow section and as the name suggests, from here you can add Shadows to your elements.

You can choose from two types of Shadows: **Outer Shadow** and **Inner Shadow**. For both, you can adjust the **Horizontal Offset**, **Vertical Offset**, **Color**, **Blur**, and **Spread**.

You can also use one of the preset shadows instead of creating one from scratch. Similarly, you can save your current shadow settings as a preset for later use.

More information on this can be found in the dedicated documentation for [Shadow](https://droip.com/docs/shadow/).

Effects
-------

Apply various Effects on your elements from this section. Effects include **Opacity**, **Blur**, **Brightness**, **Contrast**, **Saturation**, **Invert Color**, **Grayscale**, **Hue Rotate**, and **Sepia**.

You’ll also be able to change the **Cursor** style from here with a range of options to choose from.

Also, applying these effects based on specific states can help you improve the interactiveness of your website.

To find out more about this section, take a look at the documentation on [Effects](https://droip.com/docs/effects/).

Position
--------

Define the placement of your elements using the settings in the Position section. You can set the Position type as **Static**, **Relative**, **Absolute**, **Fixed**, or **Sticky**. You can also access the **Float** and **Clear** settings from here.

For more details, check out the [Position](https://droip.com/docs/position/) documentation.

Transform
---------

Using the options in the Transform section, you can manipulate an element’s appearance and placement. This feature is usually used in tandem with a specific state to add animative interactions.

Transformation options include **Move**, **Rotate**, **Scale**, and **Skew**. Use Move to shift an element’s position, Rotate to change its angle, Scale to increase or decrease its size, and Skew to change its shape.

You can also enable **3D Transformation** from here to transform elements from a 3D perspective instead.

Learn more about [Transform](https://droip.com/docs/transform/).

Transition
----------

Transitions are where you can add fluid animations to an element when it switches from one state to another. This helps make the switch less jarring and results in a better user experience.

To add a Transition, all you have to do is select the State you’ll be switching to and choose which aspect to animate. Then you can set its **Duration**, **Delay**, and **Timing Function**.

For more info, check out [Transition](https://droip.com/docs/transition/)’s dedication documentation.

Interaction
-----------

Interaction is where all the fun really happens. You can use this feature to make your website more engaging and user-friendly.

Using Interaction, there are tons you can achieve like making a dropdown menu appear and disappear on hover, animating a group of elements when you scroll down a page, expanding an image when clicked on, and so much more.

You can apply Interactions to both **Elements** and your **Page**. If you select Elements, your **Trigger** options will be the following:

* Mouse Click
* Mouse Hover
* Mouse Move Over Elements
* and Scroll Into View

If you select Page instead, your Trigger options will be:

* Mouse Move on Viewport
* While Page is Scrolling
* Page Load
* Scroll Into View
* Page Scrolled

Once you select your Object and Trigger, you can either select one of the preset responses and adjust that or create your own Custom Response. Since Droip offers a fully visual Interaction Builder, this is a pretty straightforward process.

For more in-depth information, please take a look at the [Interaction](https://droip.com/docs/interaction/) documentation where we go over the entire process step by step.

---

<!-- Source URL: https://droip.com/docs/image/ -->

---

Image

Adding images to your webpage makes your content more engaging and visually appealing for your visitors.

Use the **Image** element of Droip to add images to your webpage. This element allows you to upload an image file from your computer or choose a pre-existing image from the media library. You can also adjust the size, position, and other properties of the image.

How to Add an Image
-------------------

![How to Add an Image in Droip](https://droip.com/wp-content/uploads/2023/03/How-to-add-an-image.webp)

To add an Image element to your page, follow these simple steps:

1. Access the `Insert` > `Elements` panel and locate the Image element.
2. Drag and drop the Image element to the desired location on your canvas.
3. You can then either drag and drop your image file into this element or click on the `+ Add From Media` button to upload or choose an existing image from the media library.

Use Built-in Image Editor to Enhance Images
-------------------------------------------

![Use Built-in Image Editor to Enhance Images](https://droip.com/wp-content/uploads/2023/03/Use-Built-in-Image-Editor-to-Enhance-Images.webp)

Droip comes with built-in image editing capabilities to optimize images for your website. You can crop the image to the desired size, adjust the brightness, contrast, and saturation levels, apply various filters to enhance the overall look of the image, and more!

Learn more about Droip’s [built-in](https://droip.com/docs/media-manager/)[image editor](https://droip.com/docs/media-manager/).

Applying Effects
----------------

![Applying Effects on images in Droip](https://droip.com/wp-content/uploads/2023/03/Applying-effect.webp)

Effects can be utilized to enhance an image or create a specific mood or aesthetic. Here’s a brief overview of each effect that you can apply to your image:

* **Opacity**: The opacity property controls how transparent or opaque an element is.
* **Blur**: The blur property applies a blur effect to the element, making it appear out of focus.
* **Brightness**: The brightness property adjusts the brightness of the element.
* **Contras**t: The contrast property adjusts the contrast of the element.
* **Saturation**: The saturation property adjusts the intensity of the element’s colors.
* **Invert Color**: The invert property inverts the colors of the element, making it black & white, and vice versa.
* **Grayscale**: The grayscale property removes all color from the element, leaving a grayscale image.
* **Hue Rotate**: The hue-rotate property rotates the hue of the element’s colors, giving it a different color effect.
* **Sepia**: The sepia property applies a sepia tone to the element, giving it a vintage, yellowed effect.

Adding Links to Images
----------------------

Adding links to images can be a useful way to provide additional information to users or direct them to other parts of your website or external sites. To add a link to an image:

1. Click on the `Link` icon on the image inline editor.
2. Link the image to a webpage, website, pop-up, etc.
3. Choose how the link opens, such as from the same page or in a new tab.
4. Optionally, specify the `Rel` attribute to define the relationship between the image and the linked resource.

Replacing Images
----------------

The “Replace Image” option allows you to swap an existing image with a new one:

1. Click on the `Replace Image` button.
2. Select the new image file from your computer or the media library.

Blending Modes
--------------

![Blending Modes in Droip](https://droip.com/wp-content/uploads/2023/03/Blending-Modes.webp)

Blending Modes enable you to adjust the appearance of an image by applying different blending techniques. Each blending mode has unique properties that achieve various effects.

The available blending modes are:

* **Normal**: This is the default blending mode, which means that the layer’s pixels are displayed without any blending with underlying layers.
* **Multiply**: Multiplies the base color with the blend color, resulting in a darker color.
* **Screen**: Multiplies the inverse of the base color with the inverse of the blend color, resulting in a lighter color.
* **Overlay**: Combines Multiply and Screen blending modes, depending on the brightness of the underlying layers.
* **Darken**: Compares the colors of the base and the blend layers and selects the darker of the two.
* **Lighten**: Compares the colors of the base and the blend layers and selects the lighter of the two.
* **Color Dodge**: Lightens the base color by decreasing the contrast between the base and blend colors.
* **Color Burn**: Darkens the base color by increasing the contrast between the base and blend colors.
* **Hard Light**: Lightens or darkens the underlying pixels depending on the brightness of the blend color.
* **Soft Light**: Similar to Overlay, but with a softer and more subtle effect.
* **Difference**: Subtracts the blend color from the base color, resulting in an image that highlights the differences between the two.
* **Exclusion**: Creates an effect similar to the Difference mode, but with lower contrast and less color intensity.
* **Hue**: Applies the hue of the blend color to the base color, while using the saturation and luminosity of the base color.
* **Saturation**: Applies the saturation of the blend color to the base color, while using the hue and luminosity of the base color.
* **Color**: Applies the hue and saturation of the blend color to the base color, while using the luminosity of the base color.

Image Settings
--------------

![Image Settings in Droip](https://droip.com/wp-content/uploads/2023/03/Image-Settings.webp)

First up in the Image Settings, you get a drop-down to choose how you want to display the image. These options allow you to control how an image is displayed on a website by adjusting its size and position within a designated space.

* **Fill**: This option resizes the image to fill the available space maintaining the aspect ratio of the image. Potentially cropping the image if its aspect ratio does not match the available space.
* **Contain**: This option resizes the image so that it fits within the available space without cropping the image. It always shows the whole image, even if that leaves a little space to the sides or bottom.
* **Cover**: This option resizes the image to completely cover the available space even if this means stretching or distorting the image to cover the entire space.
* **Initial**: This option sets the image to its original size, without resizing it. This means that the image will be displayed at its original dimensions, regardless of the available space.

**Rotate button**: The “rotate” option in image settings allows you to rotate an image by 15 degrees per rotation.

**Load**: Set how you want your images to load when a user visits this web page using this option.

* **Auto**: Auto set the method to load the images.
* **Eager**: Load images without delay as per usual. This is the default option.
* **Lazy**: Put off loading images until they’re nearly within viewport distance.

**Width**: Define the width of your image.

**Height**: Define the height of your image.

**Add ALT Text**: This option allows you to add alternative text that describes the content or purpose of the image. Adding alt text to images is important for accessibility and SEO.

**Attachment**: The Attachment option controls how the image is positioned relative to the surrounding content as the user scrolls the page.

It offers two values:

1. **Scroll**: With this option, the image will scroll along with the content as the user scrolls the page.
2. **Fixed**: With this option, the image will remain fixed in position on the page, even as the user scrolls.

The Attachment option can be useful for creating certain visual effects or layouts, depending on the specific design and content of the website.

For example, using the “fixed” option for a header or background image can create a parallax scrolling effect, where the background image appears to move more slowly than the rest of the content as the user scrolls, creating a sense of depth and motion. On the other hand, using the “scroll” option for an image within a block of text can help ensure that the image remains in the correct position relative to the text as the user scrolls.

---

<!-- Source URL: https://droip.com/docs/lightbox/ -->

---

Lightbox

Lightbox combines the features of a Modal and a Slideshow. It allows you to embed an Image Gallery into your canvas, creating an engaging and interactive user experience.

Lightbox vs. Slider
-------------------

While both Lightbox and Slider components can display multiple images and videos on your webpage, there’s a crucial difference. The Slider is an integral part of the main web page, while the Lightbox appears as a popup window triggered by a specific action, with only its thumbnail visible on the main page.

Why Use a Lightbox
------------------

Using a Lightbox offers several advantages:

* **User-Friendly**: Lightboxes are less intrusive, allowing users to easily close them if they’re not interested in the content.
* **Attention-Grabbing**: When triggered, the main screen dims, drawing focus to the Lightbox, making it the sole interactive element until closed.
* **Captions**: Lightboxes can display captions, providing valuable context for the images or videos they contain.

How to Add a Lightbox
---------------------

![How to Add a Lightbox in Droip](https://droip.com/wp-content/uploads/2023/03/How-to-add-a-Lightbox.webp)

1. Go to the `Elements` panel from the left side bar.
2. Scroll down to the `Advanced` section and drag and drop the Lightbox element onto your canvas.

### Adding a Lightbox Thumbnail

![Adding a Lightbox Thumbnail](https://droip.com/wp-content/uploads/2023/03/Adding-Lightbox-Thumbnail-1.webp)

1. Click on the `Lightbox` element to see the Lightbox icon with a `+Add From Media` button.
2. Click on this button to open the `Media Manager`.
3. Select the `image` you want to use as the Lightbox’s Thumbnail, representing what users will see on your webpage.
4. Click `Update` to add the image to your Lightbox.
5. You can change the thumbnail by clicking the `Replace Thumbnail` icon (circular arrows) in the Lightbox inline editor.

Lightbox Inline Editor
----------------------

![Lightbox Inline Editor](https://droip.com/wp-content/uploads/2023/03/Lightbox-Inline-Editor.webp)

The Lightbox inline editor appears when you select the Lightbox. It includes two icons:

* **Replace Thumbnail**: Allows you to change the Lightbox thumbnail using the Media Manager.
* **Settings Icon**: Opens the Lightbox Settings.

### Lightbox Settings

![Lightbox Settings in Droip](https://droip.com/wp-content/uploads/2023/03/Lightbox-Settings.webp)

Under Lightbox Settings, you can configure additional Lightbox properties:

* **Replace Thumbnail**: Use this button to replace the Lightbox thumbnail with a different image from the Media Manager.
* **Lightbox Type**: Choose the type of media your Lightbox will display (Image or Video).
* **Link With Same Group Lightbox**: Enable this option to group your Lightbox with others. Enter the group name in the text field.

### Adding Items to a Lightbox

![Adding Items to a Lightbox ](https://droip.com/wp-content/uploads/2023/03/Adding-items-to-a-Lightbox.webp)

1. Open the `Lightbox Settings` by clicking the ellipsis icon in the inline editor.
2. Click `+ Add` next to the Lightbox Type options to open the `Media Library`.
3. Select or upload your `Lightbox Item` and click `Update` to add it.
4. Repeat these steps to add more items.

### Rearranging and Customizing Items

**Rearrange Items:** Once the Items have been added, you can rearrange their sequence by clicking and dragging on the four-dotted icon on each Item’s left.

**Visibility:** On each Item’s right, you will also find an eye-shaped icon using which you can click to hide said Item so that isn’t visible in the Lightbox.

Followed by these is another ellipsis icon and by clicking on this, you’ll find the options:

* **Add Caption:** Use this option to add text to your image or video to be displayed as an overlay. Clicking on this should bring up a popup field where you can enter this text.
* **Hide:** Just like the Visibility toggle, this hides the Lightbox Item.
* **Delete:** Click on this option to remove this item from the Lightbox.

Styling Your Lightbox
---------------------

Customize your Lightbox using the options on the Style Panel. Adjust its Size, Stroke, Shadow, Position, and more to create a unique and visually appealing Lightbox.

For more detailed information on styling, please refer to the [Style Panel](https://droip.com/docs/style-panel-overview/) Overview documentation.

---

<!-- Source URL: https://droip.com/docs/values-and-units/ -->

---

Values and Units

Throughout the design process, you’ll have to work with various values and units available in Droip.

This document will give you a complete overview of these units and how or where to apply them.

Length Units
------------

![Lengths unit stroke](https://droip.com/wp-content/uploads/2023/09/Length-Units-stroke.webp)

Below is the list of the Length Units available on Droip. These can fall under two categories: Absolute Length and Relative Length.

### Absolute Lengths

![Absolute Lengths](https://droip.com/wp-content/uploads/2023/09/Length-UnitsSize.webp)

Absolute Lengths are fixed lengths that do not depend on any other factor. Hence, these will appear exactly as defined. Below is a list of the options available for this type:

**Px (Pixel)**

1 **Pixel** = 1/96th of 1 Inch

**Pt (Point)**

1 **Point** = 1/72th of 1 Inch

### Relative Lengths:

Relative Lengths are lengths that vary depending on some other property. These help in designing responsive websites as it implements relative sizing.

Relative Sizing is when elements increase or decrease automatically based on other factors.

Below you’ll find all of the Relative Lengths available on Droip:

**Em**

Relative to the font size of the element for other properties like width and relative to the font size of the parent for typographical properties like font size.

**Rem (Root Em)**

Relative to the font size of the root element.

**VH (Viewport Height)**

Relative to 1% of the height of the Viewport. A viewport is the window’s visible area that displays the web content.

**VW (Viewport Width)**

Relative to 1% of the width of the viewport. A viewport is the window’s visible area that displays the web content.

**% (Percentage)**

Relative to the parent element. Basically, it’s the fraction of its parent element’s value.

For instance, if you set the Width of an element using the Percentage unit, then it’ll be based on the Width of its parent element.

**Auto**

Relative to the width of the content.

**Fr (Fraction)**

1 **Fraction** is one part of the whole. 1 fraction is 100% of the available space, 2 fractions are 50% each, and so on.

Color Units
-----------

![Color units](https://droip.com/wp-content/uploads/2023/09/Color-Units.webp)

Next up are Color Units. Colors are used everywhere from **Typography Color** to the color of the **Background** and more.

Below are the units available on Droip that you can use to define these colors on Droip:

**RGB**

The RGB Color Model is an additive model in which the three primary colors of light — Red, Green, and Blue are added in various ways to form a range of other colors.

In an RGB value, each number is basically an indication of how intense the red, green, and blue are in the particular color it’s representing. These values range from 0 to 255.

**HEX**

A Hex Code is a Hexadecimal RGB Value that starts with a # character followed by 6 symbols each of which can range from one of 16 values between 0 to F (which represents 15).

Each of the 2 symbols after the hash is used to represent a color value from 0 to 255 used in RGB. So the first two are for Red, the next two are for Green, and the last two are for Blue.

RGB Value to Hex Conversion:

1. The ‘R’ value is divided by 16. If the quotient (integer) of this result is below 10, then it’s written down directly after the hash. If not then its corresponding alphabet is written.
2. Then we have the remainder (If this is in decimal, it’s multiplied by 16). If this result is below 10, it’s written down next. If not, then its corresponding alphabet is what’s written.
3. The same is done for the ‘G’ and ‘B’ values until you have 6 alpha-numeric symbols following the hash.

Example:

RGB: 204, 102, 153

1. 204/16 = 12.75 | 12 > 10 => **C** | 0.75\*16 = 12 > 10 => **C**
2. 102/16 = 6.375 | 6 < 10 => **6** | 0.375\*16 = 6 < 10 => **6**
3. 153/16 = 9.5625 | 9 < 10 => **9** | 0.5625\*16 = 9 < 10 => **9**

So RGB (204, 102, 154) = **#CC6699**

Angle Units
-----------

![Angle units](https://droip.com/wp-content/uploads/2023/09/Angle-Units.webp)

Define the angle for options like **Rotate Transform**, **Hue Rotate Effect**, etc using the following units:

**Deg (Degree)**

Ranges from 1 to 360 degrees where 0 and 360 are the same.

**Rad (Radian)**

1 Rad is equal to 180/π degrees or approx 57.3 Deg.

**Grad (Gradian)**

1 Grad is 1/400 of a full circle.

**Turn**

1 Turn is equal to 360 Deg i.e. 1 entire rotation.

Time Units
----------

![time units](https://droip.com/wp-content/uploads/2023/09/Time-Units.webp)

Use the following Time Units to define the Time Duration & Delay in **Transitions** and **Interactions**.

**S (Second)**

1 Second is 1/60th of a Minute.

**Ms (Millisecond)**

1 Millisecond is 1/1000th of a Second.

Numbers
-------

Certain values in Droip have no unit and are simply numerical values. Some examples are Scale Transform, Repeat Count in Interaction, Pagination in Collection, etc.

---

<!-- Source URL: https://droip.com/docs/elements-overview/ -->

---

Elements Overview

Elements are the building blocks of a webpage, and you can configure and customize these to suit your needs using the various options available on the Style Panel.

In this documentation, we will briefly go over the Elements Panel, show you how to add an element, how to style an element, and more!

Elements Panel
--------------

![Elements Panel in Droip](https://droip.com/wp-content/uploads/2023/07/basic-2.webp)

To access the Elements Panel, click on the Elements tab on the Topbar. You should see this panel on the left side of your screen, containing all of the elements that you can use.

Speaking of, Droip offers 33 different elements covered across the following 5 categories:

1. **Layout**: Consists of elements that you can use to build the structure of your webpage.
2. **Basic**: This section contains elements that you most commonly need.
3. **Media**: Here you’ll find your media elements to add images, videos, SVG, etc.
4. **Forms**: Consists of all form-related elements like form blocks, labels, input fields, etc.
5. **Advanced**: This section contains reusable modular building blocks called components that perform a specific function or display a particular piece of content on a web page. Navigation bars, Lightboxes, Collections, and other similar elements are all examples of components.

How to Add an Element
---------------------

You can add elements to your canvas in three ways:

1. The first method is to select where you want to place your element and click on the element you want to add from `Insert` > `Elements` Panel.
2. The second method is to click and drag the element from the Elements Panel and place it where you want on the canvas.
3. Lastly, you can also drag the elements from the Elements Panel to the Layers Panel and place them where you want from there.

How to Style An Element
-----------------------

You can style these elements using the tools on the Style Panel. From here, you’ll find options to customize the following:

* Typography
* Structure
* Sizing
* Backgrounds
* Borders
* Position
* Effects
* Interactions
* Visibility Conditions

For more info, you can look at our [Style Overview](https://droip.com/docs/style-panel-overview/) documentation and the dedicated documentation for each section.

How to Duplicate the Style of an Element
----------------------------------------

To maintain consistency and save time, you can duplicate the style settings of an element. Follow these steps:

1. Select your element and open the `Class Manager` section in the `Style Panel`.
2. Click on the field and create a new `sub-class` by typing a unique name.
3. Select a different element of the same type and add the sub-class you created.
4. Elements with this sub-class will adopt the same style settings.
5. Any changes made to one element with this sub-class will update all instances with the same sub-class.

For more details on this feature, refer to our documentation on [Class Manager](https://droip.com/docs/class-manager/).

How to Reuse Elements
---------------------

Using Symbols, you can easily reuse elements or groups of elements with all their customizations intact. To convert an element or group of elements into a Symbol:

1. Select the element or wrapper element (if multiple elements) and go to `Layers` > `Symbols`.
2. Click on `Create New Symbol`, choose a Category and Name for the Symbol, and hit `Create`.
3. Now, your element(s) become a Symbol that you can repeatedly use on any page.
4. Editing the main instance of the Symbol from the Symbols Panel will update all other instances.

Check detailed information on [Symbols](https://droip.com/docs/symbols/).

---

<!-- Source URL: https://droip.com/docs/dynamic-user-lists-and-template/ -->

---

Creating Dynamic User Lists and Single User Templates

You can also use Collections to create **dynamic user lists** (e.g., authors) and custom **single user template pages** for individual users, without needing to manually update each page.

This guide will walk you through the steps to create a dynamic list of WordPress users and a single template page for individual users using Collections.

Create a Dynamic User List
--------------------------

![Create a Dynamic User List](https://droip.com/wp-content/uploads/2024/10/Create-a-Dynamic-User-List.webp)

#### **Step 1: Add a New Page for the User List**

1. Go to **Pages** and click **Add New** to create a new page where your user list will appear.
2. Title the page something like “Authors” or “Team Members” depending on your use case.

#### **Step 2: Insert the Collection List Element**

1. In the Droip editor, search for the `Collection` element.
2. In the Collection List settings, set the Collection Type to `Users`.

#### **Step 3: Customize the List**

1. The list will dynamically pull all users from the collection.
2. You can filter the list based on role and display fields such as the user’s name, profile picture, etc.

#### **Step 4: Save and Publish**

Once you’re satisfied with the layout, save the page and click **Publish**. Now you have a dynamic user list page.

Create a Dynamic Single User Template
-------------------------------------

To display individual user information dynamically, you need to create a **Single User Template** that pulls data from your user collection.

### Step 1: Create a New Template for Single Users

![Step 1: Create a New Template for Single Users](https://droip.com/wp-content/uploads/2024/10/Create-a-Dynamic-Single-User-Template.webp)

1. Go to `Pages` and click the `+ icon` and select `New Template`
2. Set the `Collection type` to `User`, and click on `Add Template` to create a new template page.

### Step 2: Display Individual User Posts Dynamically

![Display Individual User Posts Dynamically](https://droip.com/wp-content/uploads/2024/10/Display-Individual-User-Posts-Dynamically.webp)

1. Use Droip’s visual editor to design your template.
2. In the Droip editor, search for the **Collection** element.
3. Set Collection Type to `Posts` and Relation to `Inherit`.

This will dynamically pull all the posts under that user.

---

<!-- Source URL: https://droip.com/docs/versions/ -->

---

Versions

![Versions in Droip](https://droip.com/wp-content/uploads/2025/08/versions.webp)

Every page in Droip is backed by built-in version control, so you can confidently iterate, update, and restore without ever losing your work.

Whether you’re experimenting with a new layout, adjusting content, or collaborating in a team, Droip keeps a record of every published state of your page — giving you complete control over your version history.

Where to Find Version History
-----------------------------

![Where to access version history in Droip](https://droip.com/wp-content/uploads/2025/08/Where-to-find.webp)

To access your page’s version history:

1. Open any page in the Droip Editor.
2. Click the `Publish` button (top-right corner).
3. Select `Last Published`.

The **Publish History** panel will appear, showing:

* Date and time of each publish
* Author name
* Options to Rename, Restore, or Delete any version

How Versioning Works
--------------------

![How Versions work in Droip](https://droip.com/wp-content/uploads/2025/08/How-it-works.webp)

As you design, Droip autosaves your work in the current working version.

When you’re ready to push your updates live, just hit `Update`, and that version becomes your published one.

Any changes you make after clicking **Update** (i.e, publishing the page) are automatically tracked in a brand-new version. So, each time you make edits post-update:

* A new version is created and saved
* The previous version remains safely stored

This means you can freely make edits, preview changes, and go back in time if needed,  without putting your live page at risk.

### Restore a Previous Version

To revert a page to an earlier version:

1. Open the `Publish History` panel.
2. Hover over the version you want to restore.
3. Click the `More (...)` icon.
4. Select `Restore`.
5. The editor will restore the page as it was at that point in time in a new version.

### Delete Old Versions

To clean up outdated versions:

1. Open `Publish History`
2. Hover over the version you want to remove
3. Click the `More (...)` icon
4. Select `Delete`

💡 **Note**: You cannot delete the current working version or the one that’s currently published.

Things to Keep in Mind
----------------------

**Only Published Changes Create Versions**: A new version is created only when you click Update. Autosaves help preserve your progress, but they don’t appear in version history.

**You Can Preview Old Versions Without Restoring**: Use the **Play** button next to any version in the Publish History panel to view how the page looked at that time.

**Restoring Doesn’t Overwrite Your Current Work**: When you restore an older version, Droip creates a new working copy. Your previously published and working versions remain intact.

**Full Page Restores Only**: Versions represent the full state of a page at publish. You can’t restore just a section or specific element from a version.

**Keep Your History Tidy**: While there’s no hard limit on stored versions, regularly deleting outdated ones helps maintain clarity, especially on heavily edited pages.

---

<!-- Source URL: https://droip.com/docs/displaying-dynamic-content/ -->

---

Displaying Dynamic Content

Once you have created your collections and added your collection items, it’s time to display this dynamic content on your site.

By using the Collection element and Collection pages, you can efficiently manage and display your dynamic content, keeping your site both dynamic and cohesive.

Droip makes this process straightforward with the use of Collection elements and Collection pages.

Using the Collection Element
----------------------------

![Using the Collection Element](https://droip.com/wp-content/uploads/2024/08/creating-a-new-collection-1-1024x614.webp)

The Collection element allows you to display a list of items from any of your collections on any page of your site.

### Add a Collection Element

Drag and drop the Collection element onto your page where you want the list to appear.

### Select the Collection & Collection Type

Choose which collection you want to display from the dropdown menu. This could be blog posts, team members, recipes, etc.

### List Item Layouts

Choose from a variety of pre-defined layouts to display your collection items.

### Connect the Fields

![Connect the Fields](https://droip.com/wp-content/uploads/2024/08/connect-fields-3-1024x613.webp)

Select the fields you want to display within the Collection element. This can include text, images, links, and more, depending on the data in your collection.

Bind these fields to your collection data, ensuring that the displayed content updates automatically as the underlying data changes.

### Filter Collection Items

![Filter Collection Items](https://droip.com/wp-content/uploads/2024/08/filter-collection-item-1-1024x613.webp)

Filtering allows you to display specific items from your collection based on certain conditions:

Choose which collection items to display based on individual field values. For example, if your collection includes a field called “Newly Launched,” you can filter items to only display those marked as newly launched.

You can also add multiple conditions in certain fields to fine-tune which items appear. For instance, you might filter to show only items where the title is not empty and contains a specific keyword.

![Filter Collection Items with Conditions](https://droip.com/wp-content/uploads/2024/08/style-collection-1-1024x613.webp)

### Style the Collection

Use Droip’s design tools to style the Collection to match your site’s look and feel.

Creating Template Page for Collection Items
-------------------------------------------

Collection pages serve as templates for displaying individual items from your collections, ensuring that each item is presented consistently across your site. This is particularly useful for product pages, individual blog posts, portfolio entries, and more.

### Step 1: Create a Collection Page

![Create a Collection Page](https://droip.com/wp-content/uploads/2024/08/create-template-1-1024x613.webp)

1. **Access the Templates**: Navigate to the Templates section under Pages.
2. **Create a New Template**: Click the **+** icon beside Templates, select the desired post type (e.g., blog post, product), and click on **Add Template** to create a new Collection Page template.

### Step 2: Design the Template

1. **Add Elements**: Drag and drop elements onto the page to design the layout. For example, add text elements for titles, image elements for photos, and more.
2. **Bind Elements to Collection Fields**: Connect each element to the relevant fields in your collection. For instance, bind a text element to the “Title” field and an image element to the “Featured Image” field.
3. **Customize the Layout**: Adjust the layout and styling to ensure that each page looks polished and professional.
4. **Dynamic Content Display**: Each Collection Page dynamically pulls in content from the corresponding collection item, ensuring unique pages for each item.

### Step 3: Add Dynamic SEO

You can optimize the SEO for your Collection Pages by setting up dynamic titles and meta descriptions.

To do that, define a pattern for SEO titles and meta descriptions using field tags that will automatically apply to all items in the collection.

**Access SEO Settings**

![Access SEO Settings](https://droip.com/wp-content/uploads/2024/08/template-settings-1-1024x613.webp)

Click the three-dotted icon beside the template page, then click on **Settings**. Navigate to the **SEO Settings** tab to configure your dynamic SEO.

**Field Tags**

![](https://droip.com/wp-content/uploads/2024/08/template-seo-1-1024x613.webp)

Use field tags to populate SEO settings with dynamic data, ensuring each page is optimized based on its unique content.

**Open Graph Settings**: Similarly, you can dynamically set the Open Graph image, title, and description, ensuring that your content is correctly represented when shared on social media platforms.

**General Settings**: Adjust other general settings for the template page, including:

* **Page Name and URL**: Set a descriptive name and URL for the template.
* **Page Description**: Add a brief description of the page’s purpose.
* **Theme Elements Visibility**: Control the visibility of global elements like the header and footer.

Customizing a Specific Collection Item Page
-------------------------------------------

If you need to make unique changes to a specific collection item page within a Collection template, you can do that too without affecting the layout of other collection items.

This can be particularly useful if you want to highlight or customize a specific item with unique content or design elements.

**Step-by-Step Guide:**

1. **Navigate to the Collection Template Page**: Open the Droip editor and go to the Collection template page you wish to customize.
2. **Add an Element for Customization**: Drag and drop any element onto the template page where you want the unique content to appear. For example, you might add a text block, image, or any other design element.
3. **Link the Element to Dynamic Content**: With the new element selected, open the Dynamic Content Settings. Set the Type to “Post” and the Value to “Post Content”. This ensures that the element is linked to the specific collection item’s content.
4. **Access the Specific Collection Item for Editing**: Go to the specific collection item’s page in your browser. In the URL, add “?action=droip” at the end. Press Enter to reload the page in the editor mode.
5. **Customize the Collection Item Page**: The editor will now open, allowing you to make unique changes to that specific collection item. Any modifications made here will only affect this particular item, leaving the rest of the collection pages untouched.

---

<!-- Source URL: https://droip.com/docs/navbar/ -->

---

Navbar

What Is a Navbar
----------------

As its name suggests, a Navbar, short for Navigation Bar, is an element that helps users navigate a website quickly and efficiently. It’s basically a list of links that builds off of a standard HTML list but boasts a better look and functionality.

Navbars come in various forms. They can be implemented vertically or horizontally, and they can even be fixed or dynamic. Some Navbars include not just text but also graphics, videos, etc. Their design all depends on the needs of a website and its users.

Why Use a Navbar
----------------

A Navbar helps users find their destination easily on any website. Through links and sub-links listed on the Navbar, they can quickly visit their target page without needing to remember its URL. Of course, for a Navbar to be helpful, it needs to be well-designed.

### What Makes a Well-Designed Navbar

A user-friendly Navbar is one of the main factors that lead to a website’s success, so keep that in mind when designing your own. A good Navbar combines many things like choosing the most helpful links, having simple text, keeping a consistent and noticeable style, and more.

In essence, you need to think hard about what would help your users the most and design it with this in mind.

How to Add a Navbar
-------------------

To add a Navbar, do the following:

* From the left sidebar, go to `Insert > Elements` to open the `Elements` panel.
* Scroll down to the `Advanced` section and find the `Navigation` element.
* Click to add it directly to your canvas or drag and drop where you need it.

![How to Add a Navbar](https://droip.com/wp-content/uploads/2023/03/droip-how-to-add-a-nav-bar.webp)

Once you’ve added the Navbar element, you’ll notice its inline editor has the following options:

* Nav Items
* Nav Options
* More Options

Let’s break down what each of these settings allows you to customize.

### Nav Items

First up, we have the Nav Item settings.

**Add Item**: Click on this option to add new items to your navbar.

Once added, you can easily drag and drop the added items to rearrange their order in the navbar.

![Nav Items](https://droip.com/wp-content/uploads/2023/03/droip-nav-items-settings.webp)

Additionally, you can click on the ellipsis icon beside each of the items to access the following individual item settings:

* **Settings**: Access the link settings for each item from here. These settings are explained later in this documentation.
* **Move to Dropdown**: Use this option to add a menu item to another item’s submenu. A submenu is a dropdown list that appears when you hover or click on a menu item. This is further explained later in this documentation.
* **Duplicate**: Select this option to duplicate this menu item.
* **Rename**: Select this option to rename this menu item.
* **Delete**: Select this option to delete this menu item.

### Nav Options

![Nav Options](https://droip.com/wp-content/uploads/2023/03/droip-nav-options.webp)

Next, we have the Nav Options or Layout options.

**Show Sub Nav**: Define the submenu behavior from here.

* **Mouse  Hover**: Dropdown appears when the mouse hovers over a parent menu item.
* **Mouse Click**: Dropdown appears on clicking a parent menu item.
* **Always**: Dropdown always remains visible. Select this option if you want the sub-menu to stay open at all times.

**Mobile Hamburger**: Configure the Navbar responsiveness on mobile devices from here.

When enabled, the navigation menu will collapse into a hamburger menu on smaller screens. This makes for better responsiveness on mobile devices.

Once enabled, you’ll have the following additional settings appear:

**Type**: Define how the hamburger menu options will appear.

* Drop Down: The menu opens directly below menu bar.
* Drop Down Right: The menu opens on the right of the menu bar.
* Drop Down Left: The menu opens on the left of the menu bar.

**Menu Icon:** Choose which screen sizes will display the hamburger menu.

* **All Device**: Hamburger menu enabled for all devices.
* **Tablet and below**: Hamburger menu displayed on tablets and smaller screens.
* **Mobile Landscape and below**: Hamburger menu displayed on mobile landscape mode and smaller screens.
* **Mobile and below**: Hamburger menu displayed on mobile and smaller screens.

**Hide Delay**: Set how long to wait before the hamburger menu hides after the close icon is clicked.

**Show Mobile Menu:** Enable this option to force the mobile menu to be visible, useful for previewing how the navbar looks on smaller screens.

### More Options

![More Options](https://droip.com/wp-content/uploads/2023/03/droip-more-options.webp)

Lastly, we have More Options, which is common for all elements in Droip.

* **ID**: Set a unique identifier for the navigation element. It can be used in CSS or JavaScript to style or manipulate the element. Make sure to use descriptive IDs for easy identification and styling.
* **Tag**: Specify the HTML tag for the element. In this case, it’s set to , which is the semantic tag for navigation menus.
* **Area Label**: This is for ARIA (Accessible Rich Internet Applications) labeling. It provides an accessible name for screen readers, helping users with disabilities understand the purpose of the navigation.
* **Tab Index**: Set the keyboard navigation order. Only use it when you need a custom tab sequence.
  + 0 means it follows the natural order of the document.
  + A positive number (1, 2, etc.) means it will be focused in a specific order before elements with a lower number.
  + -1 makes the element focusable only through JavaScript.
* **Access**: Set who can access the navigation element. Options include:
  + All (default)
  + Guest
  + Logged In
  + Adminitrator
  + Editor
  + Author
  + Subscriber
* **Add New Attributes**: Manually add custom attributes like data-\*, aria-\*, or other HTML properties as needed.

How to Make a Navbar Sticky
---------------------------

![How to Make a Navbar Sticky](https://droip.com/wp-content/uploads/2023/03/droip-how-to-make-navbar-sticky.webp)

Making a Navbar sticky is always a good choice, especially if your webpage is on the longer side, as it makes it easier for users to navigate your website without having to scroll all the way up to access it.

It also allows them to stay in the same spot on their current page while also opening a different link from the Navbar in a new tab or window.

**To make your Navbar sticky, do the following**:

1. Select the Navbar and head to the `Style Panel > Position`.
2. Set the `Position` to **Sticky**, the `Top Offset` to **0%**, and the `Left Offset` to **50%**.
3. Set the `Z-Index` value to 100 to ensure the Navbar is always layered and visible above all the other elements on a page.

**📝 Note**: For this to work properly, make sure your Navbar is not within any layout element.

Creating a Mega Menu for Navbar
-------------------------------

![Creating a Mega Menu for Navbar](https://droip.com/wp-content/uploads/2023/03/droip-creating-a-mega-menu-for-navbar.webp)

To create a mega menu, follow these steps:

1. Select the Navbar element on the canvas
2. Open the `Nav Items` settings and click on `Add item`
3. Select the `Mega Menu` option

When you add a Mega Menu item, a nested `Menu Wrapper` is included by default. To add items to the Mega Menu, just drag & drop any of the existing items within this wrapper.

![Customizing a Mega Menu for Navbar](https://droip.com/wp-content/uploads/2023/03/droip-creating-a-mega-menu-for-navbar-2.webp)

The Mega Menu works just like any other submenu so you can customize how it expands by going to `Nav Options > Show Sub Nav` and choosing your preferred option.

Linking Nav Items
-----------------

Now that you’ve added your Nav Menu Items, it is time to link them to their corresponding web pages.

You can access `Link Settings` for Nav Menu Items in two ways:

* In Nav Items, select an item and click the ellipsis icon to open its Link Settings.
* Or, click directly on a Link Text element to access its Link Settings.

![Nav Item Link Settings](https://droip.com/wp-content/uploads/2023/03/droip-nav-items-link-settings.webp)

Here, you’ll find the following options:

* **Type**: Set the link type.
* **Link Target**: Specify the target destination. For example, choose a specific page for the **Page** type, enter a URL for **Web Address**, and so on.
* **Open in New Tab**: Enable this if you want the link to open in a new tab, though nav menu links typically open in the same tab.

For more details, check out the [Link Block documentation](https://droip.com/docs/link-block/).

You can follow the same steps to add links to other items on the Nav Menu.

---

<!-- Source URL: https://droip.com/docs/list-item/ -->

---

List Item

![List item of Droip](https://droip.com/wp-content/uploads/2023/09/List-Item.webp)

As the name suggests, the List Item element is used to represent an item in a List element. This list can be an ordered or an unordered list. Keep in mind that a List Item *must* have the List element as its parent.

Usually, List Items contain a text element but you can add elements like Image, SVG, etc as well.

Adding a List Item
------------------

Before adding a List Item, you’ll first need to add a [List element](https://droip.com/docs/list/) to your canvas. Follow these steps:

1. Go to the `Elements` panel by clicking on the Elements tab on the Topbar.
2. Drag and drop the `List` element onto your canvas.

Now, to add a List Item, do the following:

1. Navigate to `Elements` > `Basic`.
2. Drag and drop the `List Item` element inside the list you just added.

Note that, this List might already contain a few List Items with Text elements as dummy content. You can choose to either edit these items or remove them. To edit these Text elements, simply hover over them, double-click, and edit.

To start from scratch, select each List Item and right-click to open up the context menu. Scroll down and click on delete. Or, simply press the delete key after selecting the List Item.

Adding Content to a List Item
-----------------------------

The List Item element is a versatile container for various elements in Droip. Here’s how to add different types of content as a list item:

1. Select your desired element from the `Elements` panel.
2. Drag and drop it into the `List Item` where you want it to appear.
3. If it’s a text-type element, double-click to edit its contents.

For adding an image:

1. Drag and drop the `Image` element from the Elements panel into the targeted List Item.
2. With the Image element selected, go to `Media` in the Topbar.
3. Select a suitable image from the `Media Manager`.
4. Click on `Update` to attach it to the image element.

💡**Tip:** You can also add other media elements like **Videos**, **SVGs**, etc., in the same manner.

Styling List Item and Its Contents
----------------------------------

To make your List Items stand out, you can use the [Style Panel](https://droip.com/docs/style-panel-overview/) located on the right sidebar. It offers various styling tools like Typography, Structure, Effects, and more to enhance the appearance of List Items, whether they contain text, images, or buttons.

---

<!-- Source URL: https://droip.com/docs/getting-started/ -->

---

Getting Started

Whether you’re a beginner looking for a quick setup or an experienced designer seeking complete creative freedom, Droip offers flexible ways to build your website. This guide will help you get started with Droip and walk you through the available options.

![Getting Started with Droip](https://droip.com/wp-content/uploads/2025/03/getting-started.webp)

How to Start Building with Droip
--------------------------------

Droip offers four flexible ways to create your website. Choose the one that fits your needs:

1. Using a Template Kit (Fastest)
---------------------------------

![Pre-designed template kits in Droip](https://droip.com/wp-content/uploads/2025/02/Accessing-Templates-1-1024x613.webp)

Droip provides a growing library of ready-made templates that help users quickly build professional websites without starting from scratch.   
A Template Kit is a ready-made package with all the essential pages such as Home, About, Services, and Contact. It’s the quickest way to get your site online with minimal customization.

**How to Use a Template Kit:**

1. After installation, Go to `Templates` from the editor.
2. Choose a template that fits your needs.
3. Customize the text, colors, and images to suit your brand.
4. Launch your site quickly!

2. Using Pre-Designed Pages
---------------------------

Pre-designed pages offer individual templates like landing pages, service pages, and more. You can mix and match pages to create a unique site.

**How to Use Pre-Designed Pages:**

1. From the editor, go to `Insert` panel and select `Pages`.
2. Browse through the collection and pick the pages you want.
3. Customize the selected pages to match your brand.

3. Using Pre-Made Sections
--------------------------

![Pre-made sections in Droip](https://droip.com/wp-content/uploads/2025/03/left-panel-sections.webp)

Pre-made sections are pre-designed content blocks such as headers, about sections, testimonials, and more. Combine these sections to create a custom webpage.

**How to Use Pre-Made Sections:**

1. From the editor, go to `Insert` panel and select `Sections`.
2. Browse and select sections like **Hero**, **About**, **Testimonials**, etc.
3. Drag and drop sections to build your page.
4. Customize each section as needed.

4. Creating from Scratch (Most Flexible)
----------------------------------------

This option gives you complete creative control. You can either **copy and paste from Figma** or build your site using Droip’s **drag-and-drop elements**.

### Method 1: Figma to Droip (Copy & Paste)

[](https://droip.com/wp-content/uploads/2025/03/figma-to-droip.mp4)

1. Design your site in Figma.
2. Copy your Figma design elements.
3. Paste them into Droip using the **Figma to Droip Copy & Paste** feature.
4. Make any necessary adjustments to match your branding.

Learn more about [Figma to Droip](https://droip.com/docs/figma-to-droip/).

### Method 2: Using Built-In Elements

1. From the editor, go to `Insert` panel and select `Elements`.
2. Drag and drop elements like text, images, buttons, and more from Droip’s library.
3. Customize the layout to create a completely unique design.

Support and Resources
---------------------

If you need help, Droip offers a variety of support channels:

* **Documentation:** Check out the full documentation for in-depth guides and tutorials.
* **Community Forum:** Join the [Facebook Community](https://www.facebook.com/groups/557837446451017) to ask questions and share your experiences.
* **Contact Support:** Reach out to our [support](https://droip.com/account/tickets/#/) team directly for technical assistance.
* **Video Tutorials:** Browse through our official [YouTube channel](https://www.youtube.com/@DroipNoCode) to learn with step-by-step instructional videos.

---

<!-- Source URL: https://droip.com/docs/div/ -->

---

Div

A Div block is an incredibly versatile element that can serve various purposes and be customized according to your needs. It is commonly used to group elements together and create dividers or spaces on a web page.

![Droip Div](https://droip.com/wp-content/uploads/2023/09/Div.webp)

The Most Common Uses of Div Block Are:
--------------------------------------

* **Group Elements Together**: Use Div blocks to group multiple elements together, making it easier to manage and style them collectively.
* **Create Dividers**: Div blocks can be employed to create visual dividers between sections or content on your webpage.
* **Create Space**: While using margins is recommended for creating space, Div blocks can be used when margins are not sufficient or feasible.

How to Add a Div Block
----------------------

To add a Div element to your web page, follow these simple steps:

1. Open the `Elements` panel.
2. Drag the `Div` element from the Elements panel and drop it onto the desired location of your page.

By grouping elements inside a Div block, you can edit the elements together. Any style you apply to the Div block will also apply to the elements inside.

---

<!-- Source URL: https://droip.com/docs/translate-droip-website-with-weglot/ -->

---

How to Translate a Droip Website With Weglot

Translating your Droip website with Weglot is a truly simple and fast process.

Below is a step by step guide explaining exactly how you can translate your Droip site and have a fully multilingual web platform in minutes — no matter what plugins you have installed.

**Step 1**

Go to your admin dashboard on `WordPress > Plugins > Add New` and search for Weglot.

![WP Admin Dashboard - Add New Plugin](https://droip.com/wp-content/uploads/2024/03/1-wp-dashboard-plugins-add-new-plugin.webp)

Install and activate the Weglot plugin.

**Step 2**

You’ll then see the Weglot tab on the sidebar menu of your WordPress admin dashboard.

Click on it to finalize your configuration.

![WP Admin Dashboard - Weglot](https://droip.com/wp-content/uploads/2024/03/2-wp-dashboard-weglot.webp)

**Step 3**

Enter your unique `API Key` — available on your Weglot account dashboard (you’ll have to [create an account](https://dashboard.weglot.com/register-wordpress) to get access to this).

When prompted, select the original language and the language(s) that you’d like to translate your site into.

![Weglot Main Configuration Settings](https://droip.com/wp-content/uploads/2024/03/3-weglot-configuration.webp)

Click `Save Changes` when you’re done.

**Step 4**

Your multilingual website is live! You’ll now find that a front-end language switcher has been added to your site which you can customize without any code through your Weglot tab on your WordPress admin dashboard.

You can also view and edit all of your translations from your Weglot dashboard, under the “Translations” tab.

![Weglot Account Dashboard - Translation](https://droip.com/wp-content/uploads/2024/03/4-weglot-dashboard-translations.webp)

You can try Weglot for yourself with their [15 day free trial](https://dashboard.weglot.com/register-wordpress) – with access to all the features of a paid plan.

---

<!-- Source URL: https://droip.com/docs/breakpoints/ -->

---

Breakpoints

Breakpoints in Droip give you complete control over your website’s design and layout across different screen sizes. With breakpoints, you can customize content, test responsiveness, and create custom breakpoints to ensure your site looks and functions flawlessly on any device.

Canvas Breakpoints
------------------

![Breakpoints in Droip](https://droip.com/wp-content/uploads/2023/02/breakpoints-in-droip.webp)

Located in the center of the Topbar, the `breakpoint icons` allow you to seamlessly switch between different device views. Droip provides four default breakpoints:

* **Desktop (Default value 1400px):**Design for larger screens such as desktops and laptops. This is the default breakpoint, and any styles applied here will cascade down to all smaller breakpoints unless overridden.
* **Tablet (Default value 991px):**Optimize your design for tablet-sized screens, such as iPads. Styles applied at this breakpoint will apply to screens 991px wide and below.
* **Mobile Landscape (Default value 767px):**Tailor your website for phones held in landscape mode. Any changes made here will apply to screens 767px wide and smaller.
* **Mobile (Default 575px):**Ensure an optimal viewing experience on smaller smartphone screens. Styles applied at this breakpoint will only affect devices 575px wide and below.

Custom Breakpoints
------------------

![Unlimited custom breakpoints in Droip](https://droip.com/wp-content/uploads/2023/02/custom-breakpoints.webp)

Need more flexibility? Droip lets you add as many custom breakpoints as needed. Simply click the ellipsis icon beside the default breakpoints and set your own custom width to fine-tune your design for specific screen sizes.

How Breakpoints Work in Droip
-----------------------------

* The **Desktop** breakpoint acts as the global viewport, meaning all styles applied here will cascade down to smaller breakpoints.
* Any changes made in **Tablet view** will apply to tablet screens and smaller breakpoints unless overridden.
* The same applies to **Mobile Landscape and Mobile views**, with styles cascading downward unless explicitly changed.
* This **hierarchical approach** streamlines your design workflow, ensuring consistency across all devices.

Hiding Elements for Specific Breakpoints
----------------------------------------

Droip allows you to control the visibility of elements across different screen sizes, ensuring a responsive and optimized layout for every device.

With Droip, you can selectively **hide or show elements** based on the active breakpoint.

### How to Hide Elements for Specific Breakpoints

![How to Hide Elements for Specific Breakpoints](https://droip.com/wp-content/uploads/2023/02/hide-show-on-breakpoints.webp)

1. **Select the Element:** Click on the element you want to hide from the canvas.
2. **Switch to Your Desired Breakpoint:** Use the top-center device switcher to choose the screen size (e.g., desktop, tablet, mobile).
3. **Go to the Effects Panel:** On the right-hand sidebar, scroll down to the **Effects** section.
4. **Set Visibility:** Under the **Visibility** settings:  
   * Click on the **“Hidden”** button to hide the element for the currently selected breakpoint.
   * The element will be visually dimmed in the canvas to indicate it’s hidden.
5. **Repeat for Other Breakpoints (if needed):** Switch between other breakpoints and adjust visibility as needed.

Testing Responsiveness & Fluidity
---------------------------------

Use the **Preview** button to test your design’s responsiveness across different screen sizes. This helps ensure that your layout, typography, images, and other elements adjust smoothly across devices.

---

<!-- Source URL: https://droip.com/docs/collections/ -->

---

Collections

In Droip, a collection is a structured set of related content items that you can manage centrally and display dynamically on your website.

Collections allow you to group similar types of content, such as blog posts, projects, or team members, and manage them efficiently within the Content Manager.

Each collection is composed of individual entries, each entry being a unique instance of the content type defined by the collection.

Creating a New Collection
-------------------------

![Creating a New Collection](https://droip.com/wp-content/uploads/2024/08/creating-a-new-collection-1024x614.webp)

Step-by-Step Guide to Creating a Collection:

1. **Access the Content Manager**: Open the Droip editor, then navigate to the “Content Manager” option on the top bar.
2. **Add New Collection**: Click on the “+ Add New” button to start creating a new collection.

3. **Choose a Preset or Start from Scratch**: You can either select a collection preset (like Team Members or Recipes) to get started quickly or choose to create a custom collection from scratch.

4. **Name Your Collection**: Enter a name for your collection that clearly describes its content, such as “Blog Posts” or “Portfolio Projects.”
5. **Define the Collection URL**: Specify the URL for your collection, which will be used in your website’s address bar.

6. **Add Fields**: Define the fields for your collection. Click on the “+ Add” button under “Custom Fields” to add new fields. You can add text fields, images, videos, dates, and more, depending on what data you need to capture.

![Add collection fields](https://droip.com/wp-content/uploads/2024/08/add-fields-1024x613.webp)

7. **Configure Field Settings**: For each field, configure its settings such as label, required status, and any validation rules.
8. **Save Your Collection**: Once you’ve added all the necessary fields and configured them, click the “Create” button to save your new collection.

Collection Presets
------------------

Droip provides several collection presets to help you get started quickly with commonly used content types. These presets come with predefined fields tailored to their specific use cases, making it easy to set up and start adding content.

* **Team Members**: Includes fields for name, position, bio, profile picture, and contact information.
* **Portfolio**: Designed for showcasing projects, with fields for project name, descriptions, images, and links.
* **Projects**: Similar to the portfolio preset, focused on detailed project descriptions and related media.
* **Clients**: Includes fields for client names, testimonials, project history, and contact details.
* **Listings**: Ideal for real estate, job postings, or product catalogs, with fields for title, description, price, and location.
* **Recipes**: Comes with fields for recipe name, ingredients, steps, cooking time, and images.

### Customizing Presets

While the presets provide a solid starting point, you can customize them to better fit your specific needs:

1. **Select a Preset**: When creating a new collection, choose a preset that closely matches your requirements.
2. **Modify Fields**: After creating the collection, you can add, remove, or edit fields to suit your needs. For example, you might add a “video tutorial” field to the Recipes preset or a “client logo” field to the Clients preset.
3. **Rearrange Fields**: Adjust the order of fields by dragging and dropping them in the desired sequence.
4. **Field Settings**: Customize each field’s settings, such as making a field required, changing its label, or adding validation rules.
5. **Save Changes**: After customizing the preset, save your changes to update the collection.

By understanding and utilizing collections, you can effectively manage and display dynamic content on your Droip website.

In the next sections, we’ll delve deeper into managing entries, using dynamic content, and integrating collections into your website design.

---

<!-- Source URL: https://droip.com/docs/connect-elements-to-dynamic-fields/ -->

---

Connect Elements To Dynamic Fields

Elements by default may show some placeholder content when dropped onto the canvas which you can manually change. This type of content is what we call **Static**.

However, you can configure certain elements to display **Dynamic** content too! Outside of a Collection, this can be handy if you want to display the current post’s title, excerpt, image, related comments, taxonomies, etc.

Below is a list of the elements that can display Dynamic Content and instructions on how to go about it.

Elements That Can Display Dynamic Content
-----------------------------------------

* Heading
* Paragraph
* Button
* Link Block
* Image
* Form Element – Label

Configure Elements to Display Dynamic Content
---------------------------------------------

![Configure Elements to Display Dynamic Content](https://droip.com/wp-content/uploads/2024/02/Configure-Elements-to-Display-Dynamic-Content.webp)

Displaying dynamic content using these elements is simple. Just follow the instructions below:

1. Start by selecting the element you want to use to display dynamic content.
2. Then, from the inline editor click on the `Data Collection` icon. This will open `Dynamic Content Settings`.
3. From here, define the following:
   * **Type**: Select which type of Collection you want to show from here. Options are Post, Comment, or Terms.
   * **Value**: Select which value from the Collection you just chose that you want to fetch.

And that’s it! Now you can easily use these elements anywhere on your page with or without a Collection element and showcase dynamic data with just a few clicks.

For instance, to display the Page Title, you can just set the `Type` as Post and choose the `Value` as Title!

**📝 Note**: Again, keep in mind that these elements when used outside of a Collection, have the scope of dynamic content limited to the current page and everything related to it since you cannot define any specific Collection Item here.

---

<!-- Source URL: https://droip.com/docs/droip-templates/ -->

---

Droip Templates

Droip provides a growing library of ready-made templates that help users quickly build professional websites without starting from scratch. These templates include pre-designed pages, symbols, and site settings to ensure a seamless design experience.

Accessing Templates
-------------------

![Accessing Droip Templates within the builder](https://droip.com/wp-content/uploads/2025/02/Accessing-Templates-1.webp)

To access the template library in Droip:

1. Click on the **Templates** icon located on the left sidebar.
2. The **Templates Window** will open, displaying all available templates.
3. Browse through the categories or use the search bar to find a suitable template.

Importing a Template
--------------------

![Importing a Template in Droip](https://droip.com/wp-content/uploads/2025/02/Importing-a-Template.webp)

1. Click on a template to view its details.
2. Click the **Import** button to begin the import process.
3. A **Template Overview** popup will appear, showing what the template includes, such as:  
   * **Site Settings** (Styles, Variables, Assets, Fonts)
   * **Symbols** (Reusable elements)
   * **Pages** (Pre-designed layouts)
   * **Content Manager** (Dynamic content such as awards, works, and services)
4. Click **Proceed** to confirm the import.

Successful Import
-----------------

![Successful Import of Template ](https://droip.com/wp-content/uploads/2025/02/Successful-Import.webp)

Once the import is complete:

1. A confirmation message will appear, indicating a successful import.
2. The template elements (styles, pages, symbols, and content) will be integrated into your project.
3. Click **Done** to start editing your newly imported template.

Editing Templates
-----------------

You can edit everything in the template just like any other project. This includes changing text, modifying images, and altering design elements.

* **Modify Styles:** Use the **Variables** panel to modify global styles and fonts.
* **Edit Pages:** Navigate to the **Pages** panel to customize individual pages.
* **Reuse Symbols:** Access the **Symbols** section to update shared components across your site.
* **Manage Content:** Update dynamic elements through the **Content Manager.**

You can set, unset, or edit the site header and footer from the Symbols section.

📝 **Note**: Any new page created in Droip after importing a template will inherit the set header and footer. While editing, you can double-click on the header or footer to make changes.

---

<!-- Source URL: https://droip.com/docs/tabs/ -->

---

Tabs

The Tabs element, analogous to browser tabs, facilitates the organization of multiple “Divs” within a confined space. It is particularly useful for single-page websites or instances with limited available space.

The Tabs element comprises three components: the **Tab Menu**, **Tab Content**, and **Tab Panes**. The Tab Menu allows users to navigate and access the content of each tab.

How to a Add Tab
----------------

![How to a Add Tab in Droip](https://droip.com/wp-content/uploads/2023/03/How-to-Add-a-Tabs.webp)

To add a Tab on your webpage:

1. Go to the `Elements Panel` from the left sidebar.
2. Then, scroll down and drag the `Tabs` element to your page.

Tab Settings
------------

![Tab Settings in Droip](https://droip.com/wp-content/uploads/2023/03/Tab-Settings.webp)

Now, let’s go overhow you can customize your Tabs and also add new Tab items if needed.

To do this, select the Tabs element and then click on the settings icon to open the **Tab Settings**.

**Add New Tab:** Click on the `+ Add` icon to add a New Tab item. You’ll see this New Tab item added to the Tabs element on the Tabs Menu and also find its alias on the Tab Settings window.

**Reorder Tabs:** To rearrange Tab items, simply drag it to the desired position.

Then, click on the ellipsis icon that’s beside each tab item to open the action menu and  access the following options:

* **Set As Active:** Setting a Tab as Active will make sure this Tab is the one that users see when the page loads. A circular tick mark will appear beside the Tab item to signify this change.

* **Duplicate:** Use this option to easily clone any of your existing Tab items. Once you’ve selected the `Duplicate` option for the Tab item you want to clone, an identical copy of this Tab item will appear on the Tab Menu.

* **Rename:** To rename a Tab, choose the `Rename` option, enter the new name, and hit `save`.

* **Delete:** Click on this option to delete a Tab item.

**Animation:** Set the entry transition style of the Tab content.

* **Easing**: Easing refers to the rate of change of an animation’s speed. It controls the acceleration and deceleration of the animation, affecting its overall smoothness. Options typically include linear, ease, ease-in, ease-out, and ease-in-out. Choose the easing function that best complements your animation’s style.
* **Duration**: Indicate the animation’s length.

Adding Tab Content
------------------

The Tabs element remains incomplete without content to display. Adding content to the Tabs is a straightforward process:

1. Select the `Tab` where you wish to add content by opening the `Tabs Settings` and clicking on the desired Tab item.
2. Access the `Elements Panel`, and choose the element you want to include (e.g., image element, grid element, etc.).
3. Drag and drop the selected element into the `Tabs Pane`. Customize the element as needed using the options available on the [Style Panel](https://droip.com/docs/style-panel-overview/).
4. Repeat the process for other Tabs to add content to each of them.

---

<!-- Source URL: https://droip.com/docs/collection-fields/ -->

---

Collection Fields

Each field type can be configured in the Content Manager interface, allowing you to tailor the data entry process to your specific needs.

Basic Fields
------------

![Basic fields in collection](https://droip.com/wp-content/uploads/2024/08/basic-fields-1024x614.webp)

Basic fields in the Content Manager are essential for defining the structure of your content. The two mandatory basic fields are:

* **Name**: This field is used to specify the title or name of the entry.
* **Slug**: This field is used to define a URL-friendly version of the name, which helps in creating clean URLs for your content.

These fields are automatically included when you create a new collection item and are essential for organizing and referencing your content.

Custom Fields
-------------

![Custom fields in collection](https://droip.com/wp-content/uploads/2024/08/custom-fields-1024x613.webp)

Custom fields allow you to extend the functionality of your collections by adding specific types of data that suit your needs.

### Text Field

**Purpose**: For adding short pieces of text.

**Configuration**: Specify the field label, help text, and validation rules such as required or maximum length.

* Required: Tick to set the field as mandatory.
* Character Limit: Specify the maximum number of characters allowed.
* Required: Tick to set the field as mandatory.
* How to display: Connect the text field to a heading, paragraph, or any text element.

### Rich Text Field

**Purpose**: For adding formatted text with various styling options.

**Configuration**:

* Formatting Tools: Enable options like bold, italic, lists, links, and more.
* Word Count: Set a word limit for the content.
* Required: Tick to set the field as mandatory.
* How to display: Connect the text field to a heading, paragraph, or any text element.

### Image Field

**Purpose**: For uploading and displaying images.

**Configuration**:

* Image Formats: You can accept all formats or choose JPG, PNG, or GIF.
* Size Limitations: You can set the minimum and maximum file size allowed.
* Required: Tick to set the field as mandatory.
* How to display: Connect the image field to an image element.

### Video Field

**Purpose**: For embedding video content.

**Configuration**:

* Video Formats: You can choose to accept from MP4, MOV, AVI, or all.
* Video Type: You can set it to upload a file or insert a URL
* Size Limitations: You can set the minimum and maximum file size allowed.
* Required: Tick to set the field as mandatory.
* How to display: Connect the video field to a video element.

### Email Field

**Purpose**: For storing email addresses.

**Configuration**:

* Required: Tick to set the field as mandatory.
* How to display: Connect the email field to any text or link element.

### Phone Field

**Purpose**: For storing phone numbers.

**Configuration**:

* Required: Tick to set the field as mandatory.
* How to display: Connect the phone field to any text or link element.

### Number Field

**Purpose**: For storing numerical values.

**Configuration**:

* Number format: Select decimal or integer format or both
* Allow negative number: Tick to allow negative number
* Required: Tick to set the field as mandatory.
* How to display: Connect the to any text or link element.

### Date Field

**Purpose**: For selecting dates.

**Configuration**:

* Default Date: Specify a default date if needed.
* Required: Tick to set the field as mandatory.
* How to Display: Connect the date field to text element on your site.

### Time Field

**Purpose**: For selecting times.

**Configuration**:

* Default Date: Specify a default time if needed.
* Required: Tick to set the field as mandatory.
* How to Display: Connect the date field to text element on your site.

### Switch Field

**Purpose**: To add a toggle or switch option (e.g., on/off).

**Configuration**:

* Default State: Set the default state (e.g., on or off).
* Required: Tick to set the field as mandatory.

### Option Field

**Purpose**: To select from predefined options.

**Configuration**:

* Define the options list and default selected option.
* How to Display: Connect the option field to any text element on your site.

### URL Field

**Purpose**: For storing web addresses.

**Configuration**:

* Default Value: Specify a default URL if needed.
* Help Text: Add help text to guide users on the expected input.
* Required: Check to set the field as mandatory.
* How to Display: Connect the URL field to any text or link element, enabling dynamic linking to web pages directly from your content manager.

### Reference Field

A Reference Field lets you connect a single item from one collection to another. It’s perfect for one-to-one relationships — like assigning an Instructor to a Course, or a Contributor to a Project.

### Multi-Reference Field

A Multi-Reference field forms a one-to-many relationship, where one item can link to multiple items in another collection.

This enables advanced relational setups like one course to multiple tags or multi-instructors, etc.

Learn more about [Collection References](https://droip.com/docs/collection-references/).

### Gallery Field

**Purpose:** The Gallery field in Droip allows you to upload and manage multiple images for a single collection item, ideal for showcasing media-rich content like project galleries, product photos, etc.

**Configurations:**

* Name: Name your field (e.g., Project Gallery).
* File Format: Select file format as you want: JPG, PNG, GIF, or All Format.

**Uploading Gallery Images**

When you’re adding or editing a project in your Projects collection:

1. Scroll to the Gallery field.
2. Click **Add Image**.
3. Add as many files as you want.
4. Rearrange them if needed (just drag and drop).

Note: All uploaded images are automatically optimized for performance.

**How to Display**

You can dynamically show your image galleries on any page either as part of a list (e.g., all projects) or a template (e.g., a single project page).

**On a Template Page (e.g., Single Project Page)**

1. Drag a **Collection Element** onto the canvas.
2. Set the Collection Element:

![Connect the collection to the gallery field](https://droip.com/wp-content/uploads/2024/08/Set-The-collection-element.webp)

* **Source:** Gallery
* **Name:** Your Gallery field’s name

3. Inside the Collection Element:

![Connect the collection item to display gallery](https://droip.com/wp-content/uploads/2024/08/Inside-the-collection-element.webp)

* Add an **Image** element.
* Click the **Dynamic Content** icon and set **Type** as **Gallery**

Since you’re on a template page, Droip already knows which project you’re working with. It’ll pull and display all the images from that item’s gallery field.

**On a List Page (e.g., All Projects)**

This is where you need to be intentional. Only use it wheneach list item benefits from visual storytelling or you want to show multiple images at a glance (e.g., portfolios, properties, etc.).

1. Add a **Collection Element** to the page.
2. Set the **Source** as **Posts** and **Type** as Projects (or your collection name).
3. Inside that Collection Element, add another **Collection Element**. This nested element will display the gallery images.
4. Set the nested Collection Element:

* **Type:** Gallery
* **Name:** Your Gallery field’s name

5. Inside the nested element:

* Add an **Image** element.
* Click the **Dynamic Content** icon.
* Set **Type** to **Gallery**

This will show each image in the gallery field for each project.  
  
You can dynamically limit the number of images displayed from the Gallery field on the list page using Limit from Collection List Settings.

---

<!-- Source URL: https://droip.com/docs/container/ -->

---

Container

The Container element is used for organizing content neatly toward the center of your web page. By placing content inside a container, it automatically becomes responsive, adapting to different screen sizes, unless you set a fixed width. Containers are often used within Sections (which are, by default, full-width) to align the content towards the center.

![Droip container](https://droip.com/wp-content/uploads/2023/09/Container.webp)

How to Add a Container
----------------------

To add a Container element to your web page, follow these simple steps:

1. Open the `Elements` panel in Droip.
2. Drag the `Container` element from the Elements panel and drop it onto your page canvas.
3. By default, the Container will organize the content inside it towards the center.

Change Container Width
----------------------

If you want to change the default container width and make it wider, you can do that in simply two steps:

1. Add a class to the container
2. Change the Max Width

Add Breathing Space
-------------------

Containers are full-width for mobile devices. So if you want to add some breathing space at the edge, you can add padding to the left and right.

To do this:

* Select the Container element on the canvas
* In the Style panel, add left and right padding (e.g. 20 pixels)

Reuse Container
---------------

To reuse a container with the same styling, add a class to the container and apply that class to other containers within your project:

* Select an element on the canvas
* Type in the class name in the Selector field
* Press Return to apply the class

Style Container For Different Breakpoints
-----------------------------------------

You can also style the Container for breakpoints larger than the default. If you want your Container width to be more appropriately sized for larger displays – you can do that in 4 steps:

* Click on the ellipsis icon (the three dots next to the default breakpoints) to open the **Custom Breakpoints** window
* Select any larger breakpoint option from the list or define your own
* Ensure the Container element is selected
* Adjust the max-width style to fit the selected breakpoint

📝 **Note:** Make sure to switch back to the base breakpoint when you continue to design your project.

Difference Between Div, Container, and Section
----------------------------------------------

By default, Containers and Sections are Divs with special properties.

* **Sections**: Sections are used to group a webpage into parts, with content inside usually related to a single theme.
* **Divs**: Divs are basically blocks to hold content and convey no special meaning.
* **Containers**: Containers are primarily used to keep content centered on larger displays. Unlike Containers, Sections and Divs span the entire width of the screen.

---

<!-- Source URL: https://droip.com/docs/pop-ups/ -->

---

Pop-ups

Pop-ups, also known as modals, are versatile dialog windows used to display information that requires user attention without navigating away from the main content. They are commonly used for confirming actions, providing additional information, or collecting user input.

Creating a Pop-up
-----------------

![Creating a Popup in Droip](https://droip.com/wp-content/uploads/2023/02/Creating-a-Popup.webp)

To add a Pop-up to your page:

1. Navigate to the `Pages` panel in the left sidebar.
2. Click on the `+` icon and select `New Pop-up` to create a new Pop-up.
3. Enter a name for your Pop-up, save it, and start editing.

![Save the Popup to start desiging](https://droip.com/wp-content/uploads/2023/02/Publishing-a-Popup-1.webp)

Designing a Pop-up
------------------

Using Droip Elements and various customization options, you can create Pop-ups that seamlessly integrate with your website while meeting your specific needs.

Pop-up Settings
---------------

![Popup settings in Droip](https://droip.com/wp-content/uploads/2023/02/Popup-Settings.webp)

The Pop-up Settings allow you to control various aspects of the Pop-up. Select the pop-up on the canvas and click on the `settings icon` from the inline editor editor to access the following:

### Pop-up Name

Assign a label to identify the Pop-up in the builder.

### Display Conditions

Determine where and for whom the Pop-up will appear:

**Set Display Condition to Entire Site**

![Set display conditions to entire site](https://droip.com/wp-content/uploads/2023/02/Entire-Site.webp)

The Pop-up will be displayed across all pages of the website, ensuring it reaches every visitor regardless of their navigation path.

**Set Display Condition** **to** **User Role**

![Set display conditions to user role](https://droip.com/wp-content/uploads/2023/02/User-Role.webp)

Restrict the Pop-up to specific user roles. You can select roles such as **Administrator, Editor, Author, Contributor, Subscriber**, or any custom roles available on your website.

**Set Display Condition** **to** **Posts**

![Set display condition to posts](https://droip.com/wp-content/uploads/2023/02/Posts.webp)

Choose whether to display the Pop-up on specific blog posts. You can:

* Select individual posts where the Pop-up should appear.
* Target entire post categories to ensure the Pop-up is shown on all posts within the chosen category.
* Select tags to ensure the Pop-up is shown on all posts within the chosen tags.

**Set Display Condition** **to** **Pages**

![Set display condition to Pages](https://droip.com/wp-content/uploads/2023/02/display-condition-pages-1.webp)

Select specific pages where the Pop-up will be shown. This allows for targeted messaging, such as displaying a subscription offer only on the pricing page or showing an announcement on the homepage.

### Triggers

![Select popup triggers in Droip](https://droip.com/wp-content/uploads/2023/02/Triggers.webp)

Set conditions for displaying the Pop-up:

* **On Page Load**: Display the Pop-up immediately when the page loads.
* **On Page Exit**: Show the Pop-up when the user is about to leave the page.
* **Show After:** Define a delay (in seconds) before the Pop-up appears.
* **Show Count**: Set how many times the Pop-up should be shown to the same user.

### Close Options

* **“X” Icon:** Choose whether to display the close icon.
* **Close Buttons:** Customize the appearance and functionality of close buttons.
* **Close by Clicking Outside:** Allow or prevent users from closing the Pop-up by clicking outside it.

### Animation

The **Animation** settings allow you to add motion effects to your Pop-ups for a more dynamic user experience. You can select from a library of pre-defined animations, including:

* **Fade In**: The Pop-up gradually appears on the screen.
* **Slide In**: The Pop-up slides into view from the selected direction (top, bottom, left, right).
* **Zoom In**: The Pop-up starts small and scales up to full size.
* **Bounce**: The Pop-up animates with a bouncing effect.
* **Rotate**: The Pop-up rotates into position.
* Many more animation styles are available to enhance the user experience.

You can also adjust:

* **Easing**: Control the speed curve of the animation.
* **Duration**: Set how long the animation lasts.

Pop-up Layout
-------------

**Pop-up Layout** allows precise control over the Pop-up’s positioning on the screen.

![Set the popup layout in Droip](https://droip.com/wp-content/uploads/2023/02/Popup-Layout.webp)

### Set Position

* The screen is divided into **9 equal sections** (3 columns, 3 rows).
* Assign the Pop-up to a preferred section (e.g., top-left, center, bottom-right, etc.).

### Horizontal & Vertical Offset

Fine-tune the Pop-up’s position relative to its assigned section.

Example: To position a Pop-up **50px from the top**, set **Vertical Offset** to 50px. To position it **50px from the left**, set the **Horizontal Offset** to 50px.

By adjusting these settings, you can ensure an optimal, user-friendly experience for visitors.

---

<!-- Source URL: https://droip.com/docs/canvas-control/ -->

---

Canvas Control

**Canvas Control** allows you to customize the display and behavior of the canvas while designing your website. It is represented by the `Scale Percentage` dropdown on the **Topbar**.

![Canvas control options in Droip](https://droip.com/wp-content/uploads/2023/02/canvas-control-options.webp)

Adjust Canvas Size While Editing
--------------------------------

You can easily modify the canvas size using the Scale Percentage dropdown. Available options include:

* **Scale to Default**: Resets the canvas to its default size.
* **Scale Larger**: Enlarges the canvas size.
* **Scale Smaller**: Reduces the canvas size.

Ruler and Element Visualization
-------------------------------

Enhance element alignment and visibility with these options:

* **Show Ruler**: Enable or disable rulers for accurate alignment.
* **Show Empty Elements**: Highlight empty elements on the canvas.
* **Show Element Edge**: Toggle visibility of element edges for better structure visualization.

View Guides
-----------

Canvas Control allows you to enable **Canvas View Guides**, which are vertical bars spanning from top to bottom for precise alignment. Customize them with:

* **Count**: Set the number of vertical bars.
* **Color**: Choose the color of the guides.
* **Gutter**: Adjust spacing between the guides.
* **Width**: Set the width of each guide.

View Guides are particularly useful for ensuring a structured and well-aligned layout.

With **Canvas Control**, you can tailor your workspace for a seamless and efficient website development experience.

---

<!-- Source URL: https://droip.com/docs/system-requirements/ -->

---

System Requirements

* **WordPress**: 5.0 or higher.
* **PHP**: 7.4 or higher.
* **PHP Extension**: GD | GD Library, Zip library for custom font upload.
* **Database** – MariaDB – 10.1 or later / MySQL – 5.7 or later
* **Browser** – Chrome, Firefox, Safari.  
  Internet Explorer is not supported.
* **Server Modules** – mod\_rewrite, cURL, fsockopen.

---

<!-- Source URL: https://droip.com/docs/form-data/ -->

---

Form Data

Droip provides a dedicated WordPress dashboard to manage form data efficiently. You can easily access and view all the forms you have created using the Form Block element in Droip. Additionally, you can export and analyze the data collected through these forms.

Accessing Form Data
-------------------

![Accessing Form Data Manager in Droip](https://droip.com/wp-content/uploads/2023/05/Accessing-Form-Data.webp)

To access your form data, follow these steps:

1. Go to your `WordPress Dashboard`.
2. Find the `Droip` menu.
3. Select `Form Data`.

Form List
---------

In the Form Data section, you can view all the forms you have created using the Form Block element in Droip.

For each form, click on the `three-dot` menu to access the following options:

1. **Open Form Data**: View the collected data for the selected form in a separate dashboard. Filter, sort, and perform various actions on the data.
2. **Export as .CSV**: Download the form data for the selected form as a CSV (Comma-Separated Values) file for sharing or further analysis.

Filter Form Entries
-------------------

Droip provides advanced filtering options for form entries in the WordPress dashboard. It allows users to create custom filters based on specific form fields such as Name, Phone, Email, message, etc., and then further refine their search results by applying specific conditions to find the exact information they are looking for.

### Create New Filter

To create a new custom filter, click on the `Filter` > `Add New Filter` button.

![Creating New Filter to Filter Form Data](https://droip.com/wp-content/uploads/2023/05/Create-New-Filter-1.webp)

Now, you can select specific form fields and refine your search results by applying specific conditions. You can create custom search filters on the following fields:

* Name
* Phone
* Email
* Message
* Created\_at

![Adding Filter Properties to Filter Form Data](https://droip.com/wp-content/uploads/2023/05/Apply-filter-on-fields.webp)

Here are the following conditions that you apply to the form fields in Filter:

* **Contains**: This condition searches for form entries that contain a specific text string, regardless of where the string appears within the field.
* **Starts\_with**: This condition searches for form entries where a field’s value starts with a specific text string.
* **Ends\_with**: This condition searches for form entries where a field’s value ends with a specific text string.
* **Does\_not\_contain**: This condition searches for form entries where a field’s value does not contain a specific text string.
* **Is**: This condition searches for form entries where a field’s value exactly matches a specified value.
* **Is\_not**: This condition searches for form entries where a field’s value does not exactly match a specified value.
* **Cell\_is\_not\_empty**: This condition is used to search for form entries where a specific field in the form is not empty.
* **Cell\_is\_empty**: This condition is used to search for form entries where a specific field in the form is empty

### Edit or Delete a Filter

![Editing or Deleting Form Filter](https://droip.com/wp-content/uploads/2023/05/Edit-or-Delete-a-Filter-1.webp)

To delete a custom filter, click on the `horizontal 3 dots menu` beside the filter. Here, you will get the option to edit or delete the specific filter.

Sort Form Entries
-----------------

![Sorting Form Data in Droip](https://droip.com/wp-content/uploads/2023/05/Sort-Form-Entries-1.webp)

You can also apply custom sorting conditions to form fields to filter and sort your form entries effectively. Here are the available sorting conditions:

* **New -> Oldest**: Sort form entries in ascending order based on the date and time of creation (newest first).
* **Oldest -> New**: Sort form entries in descending order based on the date and time of creation (oldest first).
* **A -> Z**: Sort form entries in ascending alphabetical order based on the selected field.
* **Z -> A**: Sort form entries in descending alphabetical order based on the selected field.

Perform Bulk Actions
--------------------

![Perform Bulk Actions on Form Data](https://droip.com/wp-content/uploads/2023/05/Perform-Bulk-Actions-1.webp)

Droip allows you to select multiple form entries and perform bulk actions like deleting or exporting them. This feature is beneficial for managing large amounts of data.

* **Delete**: Permanently remove selected form entries from your database.
* **Export**: Download selected form entries as a CSV file for further analysis.

---

<!-- Source URL: https://droip.com/docs/grid/ -->

---

Grid

A **Grid** layout lets you divide any section into rows and columns, offering a flexible and precise way to structure your page.

It allows for clean, consistent designs without using float or position values.

Understanding Grid Layout
-------------------------

**Grid Container vs Grid Items**

![Grid Container vs Grid Items](https://droip.com/wp-content/uploads/2023/02/grid-container-vs-grid-item-1.webp)

* When you add a Grid, it becomes the Grid Container.
* Any direct child of that container becomes a Grid Item.

Grid vs Flex
------------

![Grid vs Flex](https://droip.com/wp-content/uploads/2023/02/grid-vs-flex.webp)

* **Grid** is **two-dimensional** — it handles both rows *and* columns.
* **Flex** is **one-dimensional** — it arranges items in a single row *or* column at a time.

Check out our [Flex documentation](https://droip.com/docs/flex/)

Adding a Grid
-------------

![Adding a Grid in Droip](https://droip.com/wp-content/uploads/2023/02/adding-a-grid.webp)

### Option 1: From the Elements Panel

1. Open the `Elements`Panel (left sidebar).
2. Under the **Layouts** section, drag the `Grid` element onto the canvas.

### Option 2: Convert Existing Element to a Grid

1. Select the element on the canvas.
2. Go to `Style Panel` > `Structure` (right sidebar).
3. From the dropdown, select `Grid` **(multi-directional)**.

Grid Structure
--------------

​​Once your Grid is added, you can customize it via `Style Panel` > `Structure`.

### Grid Tracks

![Grid Tracks in Droip](https://droip.com/wp-content/uploads/2023/02/grid-tracks.webp)

Grid Tracks defines the number of columns and rows in the grid.

* `Column Tracks`: Right input field – sets number of columns.
* `Row Tracks`: Left input field – sets number of rows.
* Click the `link icon` between the inputs to keep row and column counts synced.

### Grid Gap

![Adjusting Grid Gap in Droip](https://droip.com/wp-content/uploads/2023/02/grid-gap.webp)

The Grid Gap property defines the space between each column or row.

* `Column-gap`: Right input field is for the gap between columns.
* `Row-gap`: Left input field is for the gap between rows.

Keep in mind that the gap is measured in pixels, but that can be changed from the drop-down list of units.

You can use the `link icon` that’s located between the two gap toggles to ensure all your columns and rows have the same gap.

📝 **Note:** Alternatively, click the Grid Controller icon at the top-right corner of the Grid. This opens a visual editor where you can drag to adjust the grid spacing (gap).

### Aligning Items with Place Items

![Aligning Items with Place Items](https://droip.com/wp-content/uploads/2023/02/aligning-items-with-place-items.webp)

Once you’ve added elements to your Grid, you can control how they are positioned within their individual grid cells using the `Place Items` settings.

You’ll find this option in the `Style Panel` > `Structure` > `Place Items` section.

You can:

* Use the **visual placement grid** to quickly set alignment
* Or select from the **dropdown menus** for fine-tuned control over horizontal and vertical alignment

**Horizontal Alignment (X-Axis)**

Controls how items are aligned **side to side** inside their grid cells.

Available options:

* **Auto**: Inherits alignment from the parent element.
* **Start**: Aligns items to the **left** of the cell.
* **End**: Aligns items to the **right** of the cell.
* **Center**: Centers items **horizontally** in the cell.
* **Stretch**: Stretches items to fill the cell’s **width**.

**Vertical Alignment (Y-Axis)**

Controls how items are aligned **top to bottom** within their grid cells.

Available options:

* **Normal**: Behaves like Stretch, except when the container has intrinsic height or aspect ratio—it acts like Start in those cases.
* **Start**: Aligns items to the **top** of the cell.
* **End**: Aligns items to the **bottom** of the cell.
* **Center**: Centers items **vertically** in the cell.
* **Stretch**: Stretches items to fill the cell’s **height**.

💡 **Tip**: Use the grid-based visual selector to apply both alignments at once. Each dot represents a position, just click to set!

Grid Controller Settings
------------------------

You can control the **width of each column** and the **height of each row** individually using the Grid Controller.

To open these settings:

![Grid Controller Settings in Droip](https://droip.com/wp-content/uploads/2023/02/grid-controller-settings.webp)

* Click the `Grid Controller icon` (top-right corner of your grid). Or, click on the icon that’s beside Grid Tracks
* Then, click any of the `track handles` (white bars on columns or rows) to bring up individual settings.

### Column Settings

With the Grid Controller open, you’ll be able to access toggles to define the width of the rows and columns. These settings can be accessed by clicking on any one of the white buttons that’s above every row and column.

![Individual Column Settings in Droip](https://droip.com/wp-content/uploads/2023/02/column-settings.webp)

The following are the options available to you in Column Settings.

**Width**: Define how wide you want your column to be from here.

**Min-Max Settings**: The dimensions of a track (column) are based on the width of the content. Listed below are the options available for this feature:

* Auto: Follows default settings. Track Width is based on the size of the container.
* Min-Content: Track Width is automatically set as the same length as the widest bit of content.
* Max-Content: Track Width is set so that all of its content can fit without it over-flowing the box or being wrapped.

**Override Min-Max**: Override min-max settings by defining the gap size (left) and the track width (right) from here.

**Fit Content**: Track Width is equal to the length of its content until it exceeds the given length in which case it will wrap the content to the next line instead.

**Repeat**: Use this option to duplicate tracks so that they’ll have the same style and width.

### Row Settings

![Individual Row Settings in Droip](https://droip.com/wp-content/uploads/2023/02/row-settings.webp)

In Row Settings, you’ll find the same options as you did for Column but for the Row Height:

**Height**: Define how tall you want your row to be from here.

**Min-Max Settings**: The dimensions of a track (row) are based on the height of the content. Listed below are the options available for this feature:

* Auto: Follows default settings. Track height is based on the size of the container.
* Min-Content: Track height is automatically set as the same length as the widest bit of content.
* Max-Content: Track height is set so that all of its content can fit without it over-flowing the box or being wrapped.

**Override Min-Max**: Override min-max settings by defining the gap size (left) and the row height (right) from here.

**Fit Content**: Track height is equal to the length of its content until it exceeds the given length in which case it will wrap the content to the next line instead.

**Repeat**: Use this option to duplicate tracks so that they’ll have the same style and height.

💡Tip: You can manage all tracks quickly using the bar at the **bottom of the Grid Controller**, where you can change total row/column count, apply uniform gaps, and delete the grid entirely.

Adding Elements to a Grid
-------------------------

![Adding Elements to a Grid](https://droip.com/wp-content/uploads/2023/02/adding-element-to-a-grid.webp)

To add elements to a Grid:

1. Open the `Elements` Panel from the left sidebar.
2. Drag and drop your desired elements onto the Grid.
3. Elements are added from left to right for each row.
4. If space runs out in the Grid, dropping an element will automatically create space for it.

Grid Item Settings
------------------

![](https://droip.com/wp-content/uploads/2023/02/grid-item-settings-1-1024x616.webp)

To adjust settings for a specific Grid Item (child element of the Grid), select the Grid Item and go to `Style Panel` > `Structure`.

Click the `Grid Items` button to access the following settings:

### Self Align

From Self Align, use the first drop-down to adjust the vertical alignment and the second to adjust the horizontal. These alignment options have already been explained above in the [Place Items](https://droip.com/docs/grid/#place-items) section.

### Item Order

Next, define the order of the item in the sequence of elements using the Item Order option.

Grid Items are counted from left to right for each row. Items with the lowest number are placed first while items with the highest number are placed last.

Spanning Grid Items Across Multiple Cells
-----------------------------------------

You can span individual Grid Items across **multiple rows, columns, or both**. This is useful for hero sections, cards of different sizes, featured content blocks, and more.

[Watch Video Tutorial.](https://www.youtube.com/watch?v=auofTiXa8hc&t=175s)

Droip provides **three powerful ways** to do this:

### 1. Explicit Placement (Manual)

Use this option when you want **precise control** over where the Grid Item starts and ends.

**How to Use:**

1. Select the `Grid Item`.
2. Go to `Style Panel` > `Structure` > `Grid Items` > `Position`.
3. Choose `Manual`.
4. Enter the grid line numbers:  
   * **Row Start**: The line where the item begins vertically.
   * **Row End**: The line where the item ends vertically.
   * **Column Start**: Where the item begins horizontally.
   * **Column End**: Where it ends horizontally.

Example: In a 3×3 grid (which has 4 column lines and 4 row lines), if you want a card to span the entire third column, set:

* Column Start: 3
* Column End: 4
* Row Start: 1
* Row End: 4

![Explicit Placement (Manual) of grid items](https://droip.com/wp-content/uploads/2023/02/explicit-placement-manual.webp)

### 2. Implicit Placement (Auto Start)

This is a quicker way to let Droip **auto-place** your item but still define how many lines it spans.

**How to Use**

![Implicit Placement (Auto Start) of Grid Items](https://droip.com/wp-content/uploads/2023/02/implicit-placement-auto-start.webp)

1. Select the `Grid Item`.
2. Go to `Structure` > `Grid Items` > `Position`.
3. Choose `Auto`.
4. Set:  
   * **Column Span**: Number of columns it should cover.
   * **Row Span**: Number of rows it should cover.

📝 **Note:** Start lines are auto-selected by the grid engine, and the item stretches from there.

### 3. Grid Area (Named Area Spanning)

For a more visual and reusable layout method, use **Grid Areas**. You define an area using cells and assign items to that area.

**How to Use:**

![Grid Area (Named Area Spanning)](https://droip.com/wp-content/uploads/2023/02/grid-area.webp)

1. Open the `Grid Controller` (click the top-right grid icon).
2. Click the `➕` icon inside the cells you want to group together. These must share a **common grid line**.
3. A named area (e.g., Area-1) will be created. You can edit and change the name if you want.
4. Select the item you want to span that area.
5. Go to `Structure` > `Grid Items` > `Placement` > `Area`. Choose the named area from the dropdown.

![Assigning Grid Area (Named Area Spanning)](https://droip.com/wp-content/uploads/2023/02/grid-area-v2.webp)

This is ideal for creating magazine-style layouts or dashboard-style interfaces where multiple items are organized in reusable blocks.

Using Layers to Rearrange Grid Elements
---------------------------------------

You can also easily rearrange your grid elements by going to the Layers tab from the Topbar.

On the Layers Panel, click on the Grid layer to collapse it. Then, click and drag the elements within to shuffle their order in the layer sequence thus altering their placement.

---

<!-- Source URL: https://droip.com/docs/collection-items/ -->

---

Collection Items

Once you’ve created a Collection, you need to populate the collection with collection items. Managing entries in the Content Manager involves various actions that help you maintain and organize your content effectively.

Adding New Entries
------------------

![Adding new collection entries](https://droip.com/wp-content/uploads/2024/08/new-entry-1024x614.webp)

1. Open Collection: Navigate to the desired collection within the Content Manager.
2. Add New Entry: Click on the “+ Add New” button.
3. Fill in Fields: Enter the required data in each field of the new entry form. For example, when adding a new team member, you might fill in fields for the name, slug, profile picture, bio summary, job title, email, and phone number.
4. Save Entry: Choose to “Publish” or “Save as Draft” and click “Create.”

Schedule Collection Items for Automatic Publishing
--------------------------------------------------

You can schedule Collection items in Droip to go live at a specific date and time. It comes handy for planning ahead and managing content releases automatically.

**How to Schedule a Collection Item**

![Schedule a Collection Item](https://droip.com/wp-content/uploads/2024/08/schedule-collection-items.webp)

1. Open the Collection item you want to schedule.
2. Click the `Save` dropdown at the top-right corner.
3. Select `Schedule`.
4. Set the desired `date and time` (based on your site’s configured time zone).
5. Click `Schedule` to confirm.

**How to Unschedule or Reschedule**

To unschedule, change the item’s status to `Save as Draft`.

To reschedule:

1. Open the scheduled item.
2. Click the `Save` dropdown.
3. Select `reschedule`.
4. Adjust the `date and time`.

Click `Schedule` to apply the new timing.

Managing Collection Items
-------------------------

Using the following features, you can efficiently manage your collection items and ensure that your collection table remains organized and up-to-date.

**Perform bulk actions**

![Perform bulk actions in Collections](https://droip.com/wp-content/uploads/2024/08/Perform-bulk-actions-1-1024x613.webp)

Perform bulk actions on multiple items simultaneously. This could include publishing, unpublishing, deleting, or moving items between collections.

**Filter Collection Items**

![Filter Collection Items](https://droip.com/wp-content/uploads/2024/08/Filter-Collection-Items-1-1024x613.webp)

Use filters to quickly find specific items based on criteria such as date of creation, status, or last modified date. This feature is particularly useful for managing large collections.

**Organize Collection Table**

![Organize Collection Table ](https://droip.com/wp-content/uploads/2024/08/Organize-Collection-Item-Table-1-1024x613.webp)

Customize the display of the item table by adding, removing, or rearranging columns based

on the fields. This allows for a more tailored and efficient content management experience.

In the next sections, we’ll cover advanced topics such as dynamic content integration and best practices for content management.

---

<!-- Source URL: https://droip.com/docs/size/ -->

---

Size

In the `Style Panel` > `Sizing section`, you can adjust the Width, Height, and other measurements for your element.

![Size Panel in Droip](https://droip.com/wp-content/uploads/2023/03/size.webp)

Customize the dimensions of your element with precision:

* **Width (W):** Set the Width of your element.
* **Height (H):** Set the Height of your element.

By default, these dimensions are defined as **auto**, meaning the element will occupy the size of the container.

**💡 Tip:** You can also adjust width and height by dragging any of the elements’ side handles.

Minimum Dimensions
------------------

Define the minimum width and height of the element from here. Here’s how this property affects the appearance of an element:

* **Width:** If the content is smaller than the minimum width, the minimum width will be applied. If the content is larger, this property is ignored, preventing the width from becoming smaller than the defined minimum.
* **Height:** Similarly, if the content is smaller than the minimum height, the minimum height will be applied. If the content is larger, this property is ignored, preventing the height from becoming smaller than the defined minimum.

Maximum Dimensions
------------------

Define the maximum width and height of the element from here. Here’s how this property affects the appearance of an element:

* **Width:** If the content is larger than the maximum width, the element’s height will automatically adjust.
* **Height:** If the content is larger than the maximum height, overflow occurs. The container handles this according to the overflow property. If the content is smaller, the maximum height is ignored, preventing height from exceeding the defined maximum.

Clip Content
------------

![Clip Content Option in Droip](https://droip.com/wp-content/uploads/2023/03/Clip-Content.webp)

By default, the Overflow of an element is set to Visible, meaning it’s not clipped and can extend outside the element’s box. However, using the **Clip Content** option, you can specify how overflow will be handled.

To enable this function, check the checkbox. You’ll have three options to choose from:

* **Hidden:** Overflow is clipped, and the clipped portion of the content is not visible.
* **Scroll:** Overflow is clipped, but a scroll bar is added to view the clipped content.
* **Auto:** If overflow is clipped, then a scroll bar is added for the remaining content.

Keep in mind that this property only works for elements with a specified height.

Fit
---

![Fit Property to Define How Replaced Content Fits its Container](https://droip.com/wp-content/uploads/2023/03/Fit.webp)

Use the **Fit** property to define how replaced content fits its container. Choose from options like:

* **Cover:** Replaced content is sized to maintain the aspect ratio while filling the whole content box of the element. If their aspect ratio does not match, then the object is cropped to fit.
* **Contain:** Replaced content is scaled to maintain the aspect ratio while fitting inside the content box of the element. The object is made to fill the box while keeping the aspect ratio.
* **Fill:** Replaced content is sized to maintain the aspect ratio while completely filling the whole content box of the element. If their aspect ratio does not match, then the object is stretched to fit.
* **Inherit:** This is a **Global** keyword. Property behaves according to this element’s parent.
* **Initial:** This is a **Global** keyword and resets a property back to its initial default.
* **None:** Replaced content is not resized.
* **Unset:** This is a **Global** keyword. For an inherited property it behaves like **Inherit** and for a non-inherited property, it behaves like **Initial**.
* **Scale-down:** The content is sized as in **None** or **Contain**, whichever version is the smallest.
* **Revert:** This is a **Global** keyword. For an inherited property it behaves like **Inherit** and for a non-inherited property, it reverts to the value specified in the browser stylesheet.

Object Position
---------------

![Object Position Property to Define Alignment of the Content](https://droip.com/wp-content/uploads/2023/03/Object-Position.webp)

The **Object Position** property defines the alignment of the content of the selected replaced element. You can open its window by clicking on the ellipsis icon beside the Fit option.

Below is a description of the two toggles used to adjust this property:

* **Right:** Define by what percentage the object will be offset to the Right.
* **Top:** Define by what percentage the object will be offset from the Top.

The initial value of this property is 50% by 50%, which positions the content at the center of the container. You can adjust these values to align your content top-left, bottom-right, etc.

You can also use the Grid Toggle to set the Object Position. Simply click on any one of the dots to make your content follow the same alignment. Below are a few examples of how this property works.

![Grid Toggle to set the Object Position](https://droip.com/wp-content/uploads/2023/03/object-position-2.webp)

---

<!-- Source URL: https://droip.com/docs/map/ -->

---

Map

The Map element allows you to embed highly interactive maps into any of your web pages. It is built using Leaflet and Openstreet Map, making it super easy to work with and customize.

How to Add a Map
----------------

To add the **Map** element, follow these steps:

1. Open the `Elements` panel.
2. Scroll down to the `Components` section.
3. Drag & drop the `Map` element onto your canvas.

Map Settings
------------

![Map settings in Droip](https://droip.com/wp-content/uploads/2023/03/Map-Settings.webp)

To customize the Map element, select it and click on the ellipsis icon in the inline editor to open the Map Settings. Here are the available options:

### Add Location

Search for the name of the location you want to display on the map. Then, select the desired result from the dropdown list.

### Zoom

Define the initial magnification level of the map. A value of 0 will display a wider area, while a value of 100 will provide a more detailed view of the specified location. You can adjust this by dragging the slider or entering a value into the field.

### Map Option

You can enable or disable the following map controls from the Map Options menu:

![Map Option in Droip](https://droip.com/wp-content/uploads/2023/03/Map-Options.webp)

* **Zoom Buttons**: Enable or disable the zoom-in `(+)` and zoom-out `(-)` buttons.
* **Street Button**: Enable or disable the street view button.
* **Fullscreen Button**: Enable or disable the fullscreen button on the map.
* **Draggable**: Enable this option to allow the map to be draggable.
* **Show Marker**: Enable this option to display the marker (geotag) that points to the specified location.

### Map Style

![Map style in Droip](https://droip.com/wp-content/uploads/2023/03/Map-Style.webp)

Choose from ten different options to set the style of your map from the Map Style menu.

---

<!-- Source URL: https://droip.com/docs/code/ -->

---

Code

Droip offers extensive customization options, but there are times when you may require additional custom blocks of code. That’s where the Code **element** comes in handy.

Using this element, you can easily add code in the form of `HTML`, `CSS`, and `Javascript` to your page. And not only can you use this to add custom code but also to embed third-party elements like Bootstrap Components, Social Buttons, Maps, and more.

Adding the Code Element
-----------------------

To add the **Code** element, follow these steps:

1. Open the `Elements` panel.
2. Scroll down to the `Advanced` section.
3. Drag & drop the `Code` element onto your canvas.

Custom Code Editor
------------------

To open the custom code editor, click on the button at its center or the ellipsis icon on its inline editor. On the resulting pop-up window, you’ll find two tabs — Code and Web URL.

### Code Tab

![Custom code element in Droip](https://droip.com/wp-content/uploads/2023/03/Code-Tab.webp)

This is the custom code editor. Here, you can directly paste your HTML, CSS, and JS code and then simply click on the `Embed` button to save.

### Web URL Tab

![Web URL tab in custom code editor](https://droip.com/wp-content/uploads/2023/03/Web-URL-Tab.webp)

Here, instead of typing in the full code, you can instead paste the URL where the block of code you want to add is written. To do that:

1. In the same pop-up window, switch to the `Web URL` tab.
2. Instead of typing the full code, paste the `URL` where the desired code is hosted. Please ensure the code is publicly accessible on the web.

How to Embed Custom Code
------------------------

Follow these steps to embed custom code:

**Step 1: Copy the Custom Code**

Start by copying the custom code you want to embed, either from your own code editor or a third-party resource. For example, consider the following HTML table:

```


| User | Country | Email |
| --- | --- | --- |
| Tessa H. | California, USA | [email protected] |
| Elend V. | Scotland, UK | [email protected] |


```

**Step 2: Add the Code Element**

1. Go to the `Elements` Panel.
2. Drag and drop the `Code` element onto your page.

**Step 3:** **Paste the Custom Code**

1. Click on the `ellipsis` icon in the Code element.
2. Switch to the `Code` tab.
3. Paste the copied code here.

**Step 4:** **Save Your Actions**

Finally, click the `Embed` button to save the custom code.

### Bonus: Adding Style

You can also Style this element by copying the Style code and going to the Pages Panel. Then, click on the ellipsis icon that’s beside the current page’s label. Select **Settings** and navigate to [Custom Code](https://droip.com/docs/custom-code/). Paste the copied style code into the **Inside  Tag** section.

To apply styles to the Code element, follow these additional steps:

1. Copy the style code.
2. Go to the `Pages` Panel.
3. Click on the `ellipsis` icon beside the current page’s label.
4. Select `Settings` and navigate to [Custom Code](https://droip.com/docs/custom-code/).
5. Paste the copied style code into the `Inside  Tag` section.
6. Save your changes.

Once it’s saved, you’ll be able to see the end result by clicking on the preview button on the top right.

Remember to exclude , , or  tags in your custom code, as they may interfere with the native code of the page and cause issues.

💡**Tip:** You can easily reuse custom code blocks by converting them into reusable elements using [Symbols](https://droip.com/docs/symbols/).

---

<!-- Source URL: https://droip.com/docs/keyboard-shortcuts/ -->

---

Keyboard Shortcuts

Droip offers quite a selection of Keyboard Shortcuts for various actions to make your website-building experience even smoother. Below is a list of all of the shortcuts that are available.

![Keyboard Shortcuts in Droip](https://droip.com/wp-content/uploads/2023/07/keyboard-shortcuts.webp)

Copy/Paste
----------

* **Cut**: `Cmd + X` – Remove the selected content and place it in the clipboard.
* **Copy**: `Cmd + C`– Copy the selected content to the clipboard.
* **Copy Element Style**: `Opt + Cmd + C` – Copy the style properties of the selected element to the clipboard.
* **Paste Inside**: `Cmd + V`– Paste the content from the clipboard at the bottom of the currently selected section.
* **Paste Inside First**: `Shift + Cmd + V` – Paste the content from the clipboard inside the currently selected section as the first element.
* **Paste Element Style**: `Opt + Cmd + V` – Apply the style properties from the clipboard to the selected element.
* **Duplicate**: `Cmd + D` – Create a duplicate of the selected element.
* **Delete**: `Delete` – Remove the selected element from the canvas.

View
----

* **Show Ruler**: `Shift + R` – Display a ruler to align your elements more accurately on the canvas.
* **Show Empty Elements**: `Shift + Cmd + M` – Show hidden empty elements on the canvas.
* **View Guides**: `Ctrl + G` – Enable canvas View Guides.
* **Preview Mode**: `Cmd + Shift + P` – Switch to preview mode to see how the website will look to visitors.
* **Guide Overlay**: `Cmd + Shift + G` – Display guides on top of the website content to aid in alignment.

General
-------

* **Add Class**: `Cmd + Return` – Add a new class to the selected element.
* **Rename Class**: `Shift + Cmd + Return` – Rename the class of the selected element.
* **Add Link**: `Cmd + Opt + L` – Create a hyperlink for the selected element.

Undo/Redo
---------

* **Undo**: `Cmd + Z` – Reverse the last action.
* **Redo**: `Cmd + Shift + Z` – Redo the last undone action.

Rotate & Flip
-------------

* **Rotate Left**: `Shift + Cmd + R` – Rotate the selected element counterclockwise.
* **Rotate Right**: `Cmd + R` – Rotate the selected element clockwise.
* **Flip Vertically**: `Shift + V` – Flip the selected element vertically.
* **Flip Horizontally**: `Shift + H` – Flip the selected element horizontally.

Scale/Zoom
----------

* **Scale Larger**: `Cmd + Plus (+)` – Increase the size of the selected element.
* **Scale Smaller**: `Cmd + Minus (-)` – Decrease the size of the selected element.
* **Scale to Default**: `Cmd + 0` – Reset the size of the selected element to its default.

Global Search
-------------

* **Quick Find**: `Cmd + /` – Search for elements, pages, posts, etc.

Arrangement
-----------

* **Move Forward**: `Cmd + Right Bracket (])` – Move the selected element one step forward in the layering order.
* **Bring to Front**: `Cmd + Opt + Right Brace (})` – Bring the selected element to the topmost layer.
* **Move Backward**: `Cmd + Up Arrow + Left Bracket ([)` – Move the selected element one step backward in the layering order.
* **Send Backward**: `Cmd + Opt + Left Bracket ([)` – Send the selected element to the bottommost layer.
* **Left Align**: `Opt + A` – Align the selected element to the left.
* **Horizontal Center Align**: `Opt + H` – Center the selected element horizontally.
* **Right Align**: `Opt + D` – Align the selected element to the right.
* **Top Align**: `Opt + W` – Align the selected element to the top.
* **Vertical Center Align**: `Opt + V` – Center the selected element vertically.
* **Bottom Align**: `Opt + S` – Align the selected element to the bottom.

Padding/Margin
--------------

* **To change 2 directions at once**: Hold `Opt` – Adjust padding or margin on two sides simultaneously.
* **To change 4 directions at once**: Hold `Shift` – Adjust padding or margin on all four sides simultaneously.

Toolbar
-------

* **Accessibility**: `A` – Access the accessibility features.
* **Make Selected Element a Symbol**: `Cmd + Shift + A` – Convert the selected element into a reusable symbol.
* **Show/Hide Left (Active) Panels**: `Z` – Toggle the display of left panels that are currently active.
* **Show Audit Panel**: `U` – Display the audit panel for website analysis.
* **Show Pages Panel**: `P` – Show the pages panel for managing website pages.
* **Show Elements Panel**: `E` – Show the elements panel.
* **Show Media Manager**: `M` – Access the media manager for managing website assets.
* **Show Component**: `D` – Display the components panel.
* **Show Layers**: `L` – Show the layers panel for managing website layers.
* **Show Symbols Panel**: `B` – Display the symbols panel for managing website symbols.
* **Create Component Modal**: `Opt + Cmd + K` – Open the component creation modal window.

---

<!-- Source URL: https://droip.com/docs/text-animations/ -->

---

Text Animations

Text Animations in Droip allow users to enhance their website’s visual appeal by adding dynamic movement to text elements. These animations help capture user attention, create engaging experiences, and add a professional touch to designs.

How to Use Text Animations
--------------------------

Follow these steps to add dynamic text animations.

### 1. Accessing Text Animations

![Accessing Text Animation in Droip](https://droip.com/wp-content/uploads/2025/03/Accessing-Text-Animations.webp)

To apply text animations in Droip:

1. **Select a Text Element:** Click on any text element within the Droip editor.
2. **Open the Interactions Panel:** Navigate to the **Interactions** panel in the **right style panel**.
3. **Add a New Interaction:** Click the **+ (Add)** icon to create a new interaction.
4. **Choose a Trigger:** Select a trigger that will activate the animation (e.g., **On Page Load, Scroll into View, Hover, Click**).
5. **Select the Animation Type:** From the animation options, choose **Text Animations** as the effect for the selected trigger.

### 2. Choose an Animation Type

![Choose a text animation type ](https://droip.com/wp-content/uploads/2025/03/Choose-an-Animation-Type-1024x616.webp)

Droip offers a variety of text animation styles to create unique effects. The available animation types include:

* **Blur** – Gradually reveals the text by transitioning from a blurred state.
* **Flip** – Rotates the text to create a flipping motion.
* **Shoot** – Animates text into place with a rapid movement effect.
* **Scale** – Expands or contracts the text for a zoom-like effect.
* **Rotate** – Rotates the text at various angles for a dynamic appearance.
* **Shake** – Adds a subtle or exaggerated shaking motion for emphasis.
* **Stagger** – Animates text progressively, creating a staggered effect.

### 3. Select the Application Type

![Select the application type for the animation](https://droip.com/wp-content/uploads/2025/03/Select-the-Application-Type.webp)

You can define how the animation applies to the text by selecting one of the following application types:

* **On Element** – The entire text block moves as a single unit.
* **On Words** – Animates each word individually within the text block.
* **On Character** – Animates each character separately, creating intricate motion effects.

### 4. Customization Options

![Customization options for text animations](https://droip.com/wp-content/uploads/2025/03/Customization-Options.webp)

Droip provides extensive customization controls to fine-tune the text animation:

* **Time** – Adjusts how long the animation lasts, from quick transitions to slow, dramatic effects.
* **Delay** – Adds a wait time before the animation starts.
* **Wait**: The pause time between each letter or word as it animates on screen.
* **Easing** – Controls the speed curve of the animation (e.g., linear, ease-in, ease-out, ease-in-out).
* **Scale** – Adjusts the size of the text dynamically, making it grow or shrink during the animation.
* **Blur** – Controls the level of blur applied to the text, allowing for smooth fade-ins or motion blur effects.
* **Skew** – Tilts or distorts the text along the X or Y axis to create a slanted effect.
* **Offset** – Shifts the starting position of the text, allowing for directional movement before settling into place.
* **Looping** – Choose whether the animation plays continuously or only once.
* **Repeat Count** – Set a specific number of times the animation should repeat before stopping.

### 5. Preview & Save

[](https://droip.com/wp-content/uploads/2025/03/Text-Animations.mp4)

Use the **Preview** button to see how the animation looks before finalizing. Once satisfied, click **Save** to apply the changes permanently.

Watch Text Animation in Action
------------------------------

See how different animation types, application styles, and custom settings come together to create a stunning visual experience.

---

<!-- Source URL: https://droip.com/docs/video/ -->

---

Video

Videos are a great way to capture visitors’ attention and keep them engaged with your website.

By using the Video element in Droip, you can quickly and easily add videos to your website and customize how they are displayed.

Adding Videos
-------------

![Adding Videos in Droip](https://droip.com/wp-content/uploads/2023/03/Adding-Videos.webp)

To add a Video element to your page, follow these steps:

1. Access the `Insert` > `Elements` panel.
2. Drag and drop the `Video` element on the canvas.

Next, effortlessly insert your video file:

1. Drag and drop the video file into the specified area.
2. Alternatively, use the `+ Add From Media` button to upload an existing video from your media library.

Embedding Videos
----------------

![Embedding Videos in Droip](https://droip.com/wp-content/uploads/2023/03/embedding-video.webp)

Embed Video is a quick and convenient way to add video content to your website, allowing you to host the video on a third-party platform while seamlessly integrating it into your site.

To embed a video, simply paste the video’s share link into the `URL` field.

After embedding a video in Droip, you can fine-tune its behavior and appearance.

Click the gear icon on the video element toolbar to open the **Video Options** panel. Here’s what each setting allows you to control:

![Embedded Video Settings in Droip](https://droip.com/wp-content/uploads/2023/03/Embedding-video-2-1.webp)

**Scale:** Determines how the video scales within its container.

* Fill: Stretches the video to fill the entire space.
* Contain: Ensures the entire video is visible without cropping.
* Cover: Fills the container by cropping the video, maintaining the aspect ratio.

**Ratio:** Sets the aspect ratio of the video frame. Ideal for maintaining visual consistency.

**Playback**: Defines how and when the video starts playing:

* Auto: Plays automatically when visible.
* Click: Plays when clicked.
* Hover: Plays when hovered.

**Controls**: Show or hide native video player controls like play/pause, volume, and scrub bar.

Video Settings
--------------

You get a slightly different set of options that give you more control over how the video is rendered and played when you upload a video:

![Video Settings in Droip](https://droip.com/wp-content/uploads/2023/03/replace-video.webp)

### Replace Video

To replace the existing video with a new one:

* Click on the `Replace Video` option.
* Select the new video file from your computer or from the media library.

### Video Display Controls

Tailor how your video is presented on your website using the Video Display Controls. These options adjust the size and position of the video within the designated space:

* **Fill:** Resizes the video to fill the available space while maintaining the aspect ratio of the original video.
* **Contain:** Resizes the video to fit within the available space without cropping, ensuring the entire video is visible.
* **Cover:** Resizes the video to completely cover the available space, even if it means stretching or distorting the video.
* **Initial:** Displays the video at its original size, unaffected by available space.

### Rotate Video

The **rotate** option allows you to rotate the video by 15 degrees per rotation.

### Attachment

The **attachment** option determines the video’s position relative to the content as the user scrolls the page:

* **Scroll:** The video scrolls along with the content as the user navigates the page.
* **Fixed:** The video remains fixed in its position on the page, regardless of user scrolling.

### Looping

Enable looping to have the video play continuously, or disable it for the video to play only once.

### Audio

Enabling audio allows the video to play with sound while disabling it mutes the video.

### Slo-Mo

Enable Slo-Mo for the video to play at a slower speed, or disable it to play at its original speed.

### Controls

Enable Controls to display video player controls (play/pause, volume, full-screen), or disable it to hide these controls.

### **Set Custom Thumbnail**

Use this option to add an image as a custom thumbnail for your video.

Play and Pause
--------------

The **Play & Pause** option in video settings allows you to control how the video starts and stops playing.

![The Play & Pause option in video settings](https://droip.com/wp-content/uploads/2023/03/play-n-pauses.webp)

### Start and End Time

Set specific start and end times to show only the desired portion of the video on your webpage.

### Play Options

Customize how the video is triggered to play:

* **Auto:** The video automatically starts playing as soon as the webpage loads.
* **Click:** Requires the user to click on the video player to initiate playback.
* **Hover:** Starts playing the video when the user hovers their mouse over the video player.

By using these play options, you can curate the video experience for your users, providing a better user experience on your webpage.

---

<!-- Source URL: https://droip.com/docs/custom-code/ -->

---

Custom Code

Apart from the plethora of elements and the various styling options on Droip, you can also add Custom Code. This is useful if you wish to customize your page further and make it your own using HTML, CSS & Javascript.

![Custom Code in Droip](https://droip.com/wp-content/uploads/2023/02/custom-code-1024x616.webp)

📝 **Note**: There may be cases where your Custom Code interferes with Droip’s performance and thus we cannot promise complete compatibility.

Compatible Code
---------------

As mentioned earlier, the compatible code that you can use is HTML, CSS & Javascript.

In the case of HTML Tags, make sure to use the appropriate opening and closing tags to ensure your code will work as it should. And, keep in mind not to include the tags , , or  in your custom code as it will cause your site/page to break.

Adding Custom Code
------------------

To add your Custom Code, head over to Pages > Settings > Custom Code. Here, you’ll find the following two text boxes:

* Inside  Tag: Enter code inside the  tag.
* Before