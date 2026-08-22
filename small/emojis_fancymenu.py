###### THIS CODE IS AI GENERATED! (Just because i was tired)
##############################################################################
##############################################################################

# ========== SETTINGS ==========
DIRECTION = "RIGHT_TO_LEFT"   # "RIGHT_TO_LEFT" or "LEFT_TO_RIGHT"
START_X = -120
START_Y = -40
STEP_X = 18
STEP_Y = 18
SMILEY_WIDTH = 15
SMILEY_HEIGHT = 17
# ================================

smileys_raw2 = [
    "🗡⛏🪓🏹🔱🎣✂🛡",
    "❤🍖🔔🪣🧪⚗🔥",
    "☺☹",
    "♧♣♢♦♡♥♤♠",
    "♫⇄⏶⏷⏏⏮⏪⏴⏸⏯⏵⏩⏭",
    "☁🌧⛈⚡☽☄☀🌊❄⭐",
    "⚓⚔☂✎✉⌂",
    "⌛⏳⌚⚐⚑☜☞",
    "☐☒☑✔❌○⏺◇◆△▲☆★",
    "⏼⏻♀♂☯☮⚠☠"
]

smileys_raw = [s[::-1] for s in smileys_raw2]

lines = [list(line) for line in smileys_raw]

# Sword
TEXT_SWORD = '''element {{
  interactable = false
  source = {smiley}
  source_mode = direct
  shadow = true
  scale = 1.0
  base_color = #FFFFFFFF
  text_border = 2
  line_spacing = 2
  enable_scrolling = false
  auto_line_wrapping = true
  remove_html_breaks = true
  code_block_single_color = #737373FF
  code_block_multi_color = #565656FF
  headline_line_color = #A9A9A9FF
  separation_line_color = #A9A9A9FF
  hyperlink_color = #0771FCFF
  quote_color = #818181FF
  quote_indent = 8.0
  quote_italic = false
  bullet_list_dot_color = #A9A9A9FF
  bullet_list_indent = 8.0
  bullet_list_spacing = 3.0
  parse_markdown = true
  table_show_header = true
  table_alternate_row_colors = true
  table_line_color = #787878FF
  table_header_background_color = #323232FF
  table_row_background_color = #282828FF
  table_alternate_row_color = #3C3C3CFF
  table_line_thickness = 1.0
  table_cell_padding = 8.0
  table_margin = 4.0
  element_type = text_v2
  instance_identifier = {text_id}
  appearance_delay = no_delay
  appearance_delay_seconds = 1.0
  fade_in_v2 = no_fading
  fade_in_speed = 1.0
  fade_out = no_fading
  fade_out_speed = 1.0
  base_opacity = 1.0
  auto_sizing = false
  auto_sizing_base_screen_width = 2560
  auto_sizing_base_screen_height = 1440
  sticky_anchor = false
  anchor_point = mid-right
  x = {x}
  y = {y}
  width = {width}
  height = {height}
  stretch_x = false
  stretch_y = false
  stay_on_screen = true
  element_loading_requirement_container_identifier = {loading_id}
  [loading_requirement_container_meta:{loading_id}] = [groups:][instances:]
  enable_parallax = false
  parallax_intensity_v2 = 0.5
  invert_parallax = false
  animated_offset_x = 0
  animated_offset_y = 0
  load_once_per_session = false
  in_editor_color = #FFC800FF
  layer_hidden_in_editor = false
  rotation_degrees = 0.0
  advanced_rotation_mode = false
  vertical_tilt_degrees = 0.375
  advanced_vertical_tilt_mode = false
  horizontal_tilt_degrees = 0.0
  advanced_horizontal_tilt_mode = false
}}'''

# All other
TEXT_OTHER = '''element {{
  interactable = false
  source = {smiley}
  source_mode = direct
  shadow = true
  scale = 1.0
  base_color = #FFFFFFFF
  text_border = 2
  line_spacing = 2
  enable_scrolling = false
  auto_line_wrapping = true
  remove_html_breaks = true
  code_block_single_color = #737373FF
  code_block_multi_color = #565656FF
  headline_line_color = #A9A9A9FF
  separation_line_color = #A9A9A9FF
  hyperlink_color = #0771FCFF
  quote_color = #818181FF
  quote_indent = 8.0
  quote_italic = false
  bullet_list_dot_color = #A9A9A9FF
  bullet_list_indent = 8.0
  bullet_list_spacing = 3.0
  parse_markdown = true
  table_show_header = true
  table_alternate_row_colors = true
  table_line_color = #787878FF
  table_header_background_color = #323232FF
  table_row_background_color = #282828FF
  table_alternate_row_color = #3C3C3CFF
  table_line_thickness = 1.0
  table_cell_padding = 8.0
  table_margin = 4.0
  element_type = text_v2
  instance_identifier = {text_id}
  appearance_delay = no_delay
  appearance_delay_seconds = 1.0
  fade_in_v2 = no_fading
  fade_in_speed = 1.0
  fade_out = no_fading
  fade_out_speed = 1.0
  base_opacity = 1.0
  auto_sizing = false
  auto_sizing_base_screen_width = 2560
  auto_sizing_base_screen_height = 1440
  sticky_anchor = false
  anchor_point = element
  anchor_point_element = {anchor_id}
  x = {x}
  y = {y}
  width = {width}
  height = {height}
  stretch_x = false
  stretch_y = false
  stay_on_screen = true
  element_loading_requirement_container_identifier = {loading_id}
  [loading_requirement_container_meta:{loading_id}] = [groups:][instances:]
  enable_parallax = false
  parallax_intensity_v2 = 0.5
  invert_parallax = false
  animated_offset_x = 0
  animated_offset_y = 0
  load_once_per_session = false
  in_editor_color = #FFC800FF
  layer_hidden_in_editor = false
  rotation_degrees = 0.0
  advanced_rotation_mode = false
  vertical_tilt_degrees = 0.375
  advanced_vertical_tilt_mode = false
  horizontal_tilt_degrees = 0.0
  advanced_horizontal_tilt_mode = false
}}'''

BUTTON_TEMPLATE = '''element {{
  button_element_executable_block_identifier = {button_block_id}
  [executable_action_instance:{action_id}][action_type:paste_to_chat] = true:{smiley}
  [executable_block:{button_block_id}][type:generic] = [executables:{action_id};]
  restartbackgroundanimations = true
  nine_slice_custom_background = false
  nine_slice_border_x = 5
  nine_slice_border_y = 5
  label = 
  navigatable = false
  widget_active_state_requirement_container_identifier = {widget_id}
  [loading_requirement_container_meta:{widget_id}] = [groups:][instances:]
  is_template = false
  template_apply_width = false
  template_apply_height = false
  template_apply_posx = false
  template_apply_posy = false
  template_apply_opacity = false
  template_apply_visibility = false
  template_apply_label = false
  template_share_with = buttons
  nine_slice_slider_handle = false
  nine_slice_slider_handle_border_x = 5
  nine_slice_slider_handle_border_y = 5
  element_type = custom_button
  instance_identifier = {button_instance_id}
  appearance_delay = no_delay
  appearance_delay_seconds = 1.0
  fade_in_v2 = no_fading
  fade_in_speed = 1.0
  fade_out = no_fading
  fade_out_speed = 1.0
  base_opacity = 0.1
  auto_sizing = false
  auto_sizing_base_screen_width = 2560
  auto_sizing_base_screen_height = 1440
  sticky_anchor = false
  anchor_point = element
  anchor_point_element = {target_text_id}
  x = -1
  y = -1
  width = 16
  height = 16
  stretch_x = false
  stretch_y = false
  stay_on_screen = true
  element_loading_requirement_container_identifier = {button_loading_id}
  [loading_requirement_container_meta:{button_loading_id}] = [groups:][instances:]
  enable_parallax = false
  parallax_intensity_v2 = 0.5
  invert_parallax = false
  animated_offset_x = 0
  animated_offset_y = 0
  load_once_per_session = false
  in_editor_color = #FFC800FF
  layer_hidden_in_editor = false
  rotation_degrees = 0.0
  advanced_rotation_mode = false
  vertical_tilt_degrees = 0.0
  advanced_vertical_tilt_mode = false
  horizontal_tilt_degrees = 0.0
  advanced_horizontal_tilt_mode = false
}}'''

def generate_id(base_name, counter):
    if base_name == 'text':
        return f"27bf5866-0c83-4218-9847-c05979c4f6{counter:02x}-17802475320{counter}"
    elif base_name == 'loading':
        return f"cb5c7efe-a9d2-48e0-9aa0-16aa1ba45d{counter:02x}-17802441022{counter}"
    elif base_name == 'button_block':
        return f"09dae8f7-4329-46bf-9f5e-d5a5d4eb8a{counter:02x}-17802438272{counter}"
    elif base_name == 'action':
        return f"a3fd031a-f183-49d1-aa2d-c79cc3d265d{counter:02x}-17802438788{counter}"
    elif base_name == 'widget':
        return f"d63e5ba4-528e-4122-852a-111975484f{counter:02x}-17802438272{counter}"
    elif base_name == 'button_instance':
        return f"edde5193-8fec-4259-b0d2-97445429b{counter:02x}-17802438272{counter}"
    elif base_name == 'button_loading':
        return f"e8d6eb82-cb46-4093-924c-a10cd22922f{counter:02x}-17802438272{counter}"
    else:
        return f"unknown-{counter}"

output = []
counter = 0
text_ids = {}  # (row, col) -> text_id
sword_id = None

for row_idx, row in enumerate(lines):
    for col_idx, smiley in enumerate(row):
        text_id = generate_id('text', counter)
        loading_id = generate_id('loading', counter)
        button_block_id = generate_id('button_block', counter)
        action_id = generate_id('action', counter)
        widget_id = generate_id('widget', counter)
        button_instance_id = generate_id('button_instance', counter)
        button_loading_id = generate_id('button_loading', counter)
        counter += 1

        if row_idx == 0 and col_idx == 0:
            # Sword
            sword_id = text_id
            text_block = TEXT_SWORD.format(
                smiley=smiley,
                text_id=text_id,
                x=START_X,
                y=START_Y,
                width=SMILEY_WIDTH,
                height=SMILEY_HEIGHT,
                loading_id=loading_id
            )
        else:
            if col_idx == 0:
                anchor_id = sword_id
                x = 0
                y = row_idx * STEP_Y
            else:
                anchor_id = text_ids[(row_idx, col_idx-1)]
                if DIRECTION == "RIGHT_TO_LEFT":
                    x = -STEP_X
                else:
                    x = STEP_X
                y = 0
            text_block = TEXT_OTHER.format(
                smiley=smiley,
                text_id=text_id,
                anchor_id=anchor_id,
                x=x,
                y=y,
                width=SMILEY_WIDTH,
                height=SMILEY_HEIGHT,
                loading_id=loading_id
            )
        text_ids[(row_idx, col_idx)] = text_id

        button_block = BUTTON_TEMPLATE.format(
            button_block_id=button_block_id,
            action_id=action_id,
            smiley=smiley,
            widget_id=widget_id,
            button_instance_id=button_instance_id,
            target_text_id=text_id,
            button_loading_id=button_loading_id
        )
        output.append(text_block)
        output.append(button_block)

print("\n".join(output))