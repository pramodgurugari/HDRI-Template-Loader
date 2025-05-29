
🔧 HDRI Template Loader – Detailed Description
📌 Purpose:
The HDRI Template Loader is a multi-functional tool built in Nuke (as a .nk script or embedded in a custom gizmo) that allows artists and lighting TDs to process and prepare HDRIs for high-end VFX workflows—both for live-action integration and full CG environments.

🛠️ Core Functionalities

🏞️ HDRI Input and Preprocessing
Load any HDRI image (usually in .exr format).
Normalize and grade the input image to match a standardized working exposure and color space (e.g., ACEScg or linear).

🌞 Sun Extraction & Isolation
Automatically or semi-automatically isolate the sun disc in the HDRI.
This allows:

Creating directional lights or spotlights that match the sun's position.

Enhanced control over sun intensity for relighting.

Replacing or modifying the sun without affecting sky/background.

Implementation: Often uses a combination of Keyer, Grade, Blur, and Roto nodes to extract the brightest region of the HDRI.

✨ Bloom and Glare Extraction
Separate and stylize the bloom/glare from the HDRI (overexposed areas like the sun or reflections).
These passes can be used to:

Enhance realism during HDRI relighting.

Simulate camera lens effects.

Reintroduce controlled glow in comp.

Implementation: Blur, Erode, Add, and custom filtering using expressions.

🧹 HDRI Cleanup and Patch
Remove unwanted elements from the HDRI (crew, gear, shadows).
Can use:

RotoPaint

GridWarp

STMap based patching

Optional integration with 2D tracking or projection-based cleanup.

🛋️🏙️ Interior and Exterior Modes
Adjustments and filtering optimized for:
Interior HDRIs (soft shadows, indoor bounce)

Exterior HDRIs (strong sun, horizon contrast)

Uses toggle switches or custom knobs in the UI to adapt processing chains.

🎥 Live Action vs Full CG HDRI Modes
Live Action Integration:
Match real plate lighting.

Grade the HDRI to film plate levels.

Full CG Lighting:

Enhance the HDRI with artistic bloom/sun.

Adjust HDRI contrast and warmth for stylized rendering.

🧠 Script-Based Dynamic Control
The Nuke script includes exposed user controls (via a Group or Gizmo) that let users:
Toggle features (e.g., Enable Sun Extraction, Bloom Control)

Adjust parameters (Exposure, Saturation, Glare Intensity)

Choose HDRI type (Interior/Exterior)

Output processed HDRI or layered passes

📤 Outputs:
Cleaned and relightable HDRI .exr or .hdr.

Optional passes:

Sun Mask

Bloom/Glare Layer

HDRI without sun

Patched/Cleaned HDRI

These outputs can be used in:

Maya (Arnold, Redshift, V-Ray)

Unreal Engine

Nuke for relighting comps

Custom LookDev tools

Capture
HDRI_



The HDRI Template Loader is a powerful and modular compositing tool designed within Nuke to facilitate the advanced processing and preparation of HDRI maps for a wide variety of visual effects applications. This tool is intended to streamline the workflow of lighting artists, compositors, and look development teams by offering a centralized environment where HDRIs can be dynamically edited, enhanced, and customized for both live-action integration and full CG (computer-generated) scenes. It is particularly useful in scenarios that require precise control over light behavior—such as when matching on-set lighting conditions, building synthetic environments, or manipulating environmental reflections and lighting behavior in rendering engines.

At its core, the HDRI Template Loader provides users with a structured interface to load high dynamic range images, typically in .exr format, and perform a variety of preprocessing operations. These include exposure normalization, color space adjustments (such as conversion to linear or ACEScg), and initial grading to prepare the image for further use in lighting and compositing. This ensures that the HDRI is calibrated and consistent across different shots or sequences, making it a reliable asset for both look development and shot-specific relighting.

One of the signature capabilities of this tool is its sun extraction and isolation module. This feature is designed to detect and isolate the brightest region of the HDRI—usually the sun or another dominant light source—using luminance keying, roto masks, and various blur and grade operations. Once isolated, the sun can be adjusted in terms of its intensity, color temperature, or position. This makes it easier to match the lighting directionality in CG renders or even replace the sun entirely with a synthetic directional light in 3D applications. Such granular control is vital when HDRIs are used as the primary lighting source in renderers like Arnold, Redshift, or V-Ray.

Additionally, the tool includes a bloom and glare extraction section, which isolates and stylizes the overexposed highlights in the HDRI—such as sun flares, reflective glints, and strong light blooms. This pass can be used either artistically or physically to reintroduce lens and glow effects in the comp, mimicking real camera artifacts and enhancing photorealism. These are extracted using soft blurs, erode/dilate filtering, and glow generation nodes, often layered back into the final HDRI as optional passes for flexible use.

A notable feature of the HDRI Template Loader is its built-in cleanup workflow, which allows users to remove unwanted elements captured during HDRI acquisition—such as crew members, gear, lighting rigs, or tracking markers. Using nodes like RotoPaint, GridWarp, and STMap, users can paint out and patch problem areas either manually or semi-automatically, ensuring the final HDRI is clean and production-ready for lighting and reflection usage in CG scenes.

The tool is also tailored to adapt to different environmental types with toggles for interior and exterior HDRIs. For interior HDRIs, the tool emphasizes bounce lighting, soft falloffs, and subtle contrast adjustments, while for exteriors, it enhances sky gradients, horizon detail, and sun sharpness. This adaptive behavior ensures that the HDRI output is optimized for the type of scene it's being used in, whether it’s an indoor architectural visualization or an outdoor VFX sequence.

Moreover, the HDRI Template Loader accommodates both live-action integration and full CG workflows. In live-action mode, the tool enables artists to grade the HDRI to match the color profile and exposure level of the real-world footage, ensuring seamless blending of CG elements into filmed plates. In full CG mode, artists can push the HDRI creatively—enhancing colors, exaggerating light sources, or applying stylistic bloom—to create bespoke environments that contribute to the cinematic look of fully rendered scenes.

Built with flexibility in mind, the script provides a custom UI with exposed controls, likely via a Group node or custom gizmo, that gives users direct access to key parameters. These controls may include file pickers for HDRI input, toggles for enabling sun and bloom extraction, sliders for controlling glare intensity, and dropdowns for switching between scene types or output modes. The output of the tool can be configured to include not only a fully processed and cleaned HDRI but also separate utility passes such as sun masks, bloom layers, and shadow-removed HDRIs. These outputs can be exported as .exr files and seamlessly imported into 3D rendering pipelines or reused in other compositing tasks.

Overall, the HDRI Template Loader serves as a comprehensive toolset for HDRI manipulation, offering robust functionality to support high-quality lighting design, compositing, and environmental grading. Its modular design ensures that it can be customized or extended as needed, and its utility spans from quick lookdev previews to complex production-level lighting pipelines.

### How to install HDRI Template Loader
Copy the script below and paste it into the menu.py file located in your .nuke folder. If the menu.py file does not exist, create a new one.

Additionally, copy the HDRI_Template.nk file into the same .nuke directory.

Once done, launch Nuke. You will see a new ProTools menu in the top toolbar.




![Capture](https://github.com/user-attachments/assets/05b6d3d8-7428-470b-b439-65a3a96967c2)
![Capdsture](https://github.com/user-attachments/assets/f5ed6e0c-cf0b-4417-9914-e0e39d476dc4)
