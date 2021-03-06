<?php

/**
 * Web proxy lists view.
 *
 * @category   apps
 * @package    web-proxy
 * @subpackage views
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
// Items
///////////////////////////////////////////////////////////////////////////////

$anchor = anchor_edit('/app/web_proxy/bypass/index', 'high');
$items['bypass']['title'] = lang('web_proxy_bypass');
$items['bypass']['action'] = $anchor;
$items['bypass']['anchors'] = array($anchor);

$anchor = anchor_edit('/app/web_proxy/exceptions/index', 'high');
$items['exceptions']['title'] = lang('web_proxy_exception_sites');
$items['exceptions']['action'] = $anchor;
$items['exceptions']['anchors'] = array($anchor);

///////////////////////////////////////////////////////////////////////////////
// Action table
///////////////////////////////////////////////////////////////////////////////

echo action_table(
    lang('web_proxy_rules'),
    array(),
    $items
);
