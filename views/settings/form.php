<?php

/**
 * Web proxy settings view.
 *
 * @category   Apps
 * @package    Web_Proxy
 * @subpackage Views
 * @author     ClearFoundation <developer@clearfoundation.com>
 * @copyright  2011 ClearFoundation
 * @license    http://www.gnu.org/copyleft/gpl.html GNU General Public License version 3 or later
 * @link       http://www.clearfoundation.com/docs/developer/apps/web_proxy/
 */

///////////////////////////////////////////////////////////////////////////////
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.  
//
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
// Load dependencies
///////////////////////////////////////////////////////////////////////////////

$this->lang->load('web_proxy');

///////////////////////////////////////////////////////////////////////////////
// Form handler
///////////////////////////////////////////////////////////////////////////////

if ($form_type === 'edit') {
    $read_only = FALSE;
    $buttons = array(
        form_submit_update('submit'),
        anchor_cancel('/app/web_proxy')
    );
} else {
    $read_only = TRUE;
    $buttons = array(
        anchor_edit('/app/web_proxy/settings/edit')
    );
}

///////////////////////////////////////////////////////////////////////////////
// Form
///////////////////////////////////////////////////////////////////////////////
// This is a bit unusual... the edit mode combines two fields (transparent and
// user authentication).

echo form_open('web_proxy/settings/edit'); 
echo form_header(lang('base_settings'));

if (! $transparent_capable) {
    echo field_toggle_enable_disable('user_authentication', $user_authentication, lang('web_proxy_user_authentication'), $read_only);
    echo field_dropdown('levels', $levels, $level, lang('base_performance_level'), TRUE);
} else if ($form_type === 'edit') {
    echo field_dropdown('mode', $modes, $mode, lang('web_proxy_mode'), $read_only);
} else {
    echo field_toggle_enable_disable('transparent', $transparent, lang('web_proxy_transparent_mode'), $read_only);
    echo field_toggle_enable_disable('user_authentication', $user_authentication, lang('web_proxy_user_authentication'), $read_only);
    echo field_dropdown('levels', $levels, $level, lang('base_performance_level'), TRUE);
}

echo field_button_set($buttons);

echo form_footer(); 
echo form_close();
